// SPDX-FileCopyrightText: 2026 cenky <cenkkgl@gmail.com>
// SPDX-License-Identifier: GPL-3.0-or-later

#include <QApplication>
#include <QDir>
#include <QFileInfo>
#include <QSettings>
#include <KColorScheme>
#include <KSharedConfig>

int main(int argc, char **argv) {
  QApplication app(argc, argv);
  app.setApplicationName("akyuu-palette-export");
  if (argc != 3) return 2;

  const QString source = QFileInfo(QString::fromLocal8Bit(argv[1])).absoluteFilePath();
  if (!QFileInfo(source).isFile() || !QFileInfo(source).isReadable()) return 2;
  const auto config = KSharedConfig::openConfig(source, KConfig::SimpleConfig);
  if (!config->hasGroup("Colors:Window") || !config->hasGroup("Colors:View")) return 2;
  auto palette = KColorScheme::createApplicationPalette(config);
  for (auto group : {QPalette::Active, QPalette::Inactive, QPalette::Disabled})
    palette.setColor(group, QPalette::Accent, palette.color(group, QPalette::Highlight));

  const QDir output(QDir(QString::fromLocal8Bit(argv[2])).absolutePath());
  for (const int version : {5, 6}) {
    const auto directory = QString("qt%1ct").arg(version);
    if (!output.mkpath(directory)) return 3;
    QSettings settings(output.filePath(directory + "/Akyuu.conf"), QSettings::IniFormat);
    settings.beginGroup("ColorScheme");
    for (auto group : {QPalette::Active, QPalette::Inactive, QPalette::Disabled}) {
      QStringList colors;
      const int count = version == 5 ? 21 : 22;
      for (int role = 0; role < count; ++role)
        colors << palette.color(group, static_cast<QPalette::ColorRole>(role)).name(QColor::HexArgb);
      const auto key = group == QPalette::Active ? "active_colors"
                     : group == QPalette::Inactive ? "inactive_colors" : "disabled_colors";
      settings.setValue(key, colors);
    }
    settings.endGroup();
    settings.sync();
    if (settings.status() != QSettings::NoError) return 4;
  }
}
