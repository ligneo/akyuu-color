# Installation

Run these commands from the repository directory. Installing the files makes
the palette available; select Akyuu in the relevant settings afterward.

## KDE Plasma

```sh
install -Dm644 Akyuu.colors "${XDG_DATA_HOME:-$HOME/.local/share}/color-schemes/Akyuu.colors"
```

Open **System Settings → Colors & Themes → Colors** and select **Akyuu**.
Some Plasma versions use different settings categories; search for Colors.
Plasma applies the scheme to applications using its platform theme.

A KDE application with its own color-scheme menu can also select Akyuu directly.
For example, Dolphin provides **Settings → Color Scheme → Akyuu**.

## Qt 5 with qt5ct

Install qt5ct using your distribution's package manager, then copy the palette:

```sh
install -Dm644 qt5ct/Akyuu.conf "${XDG_CONFIG_HOME:-$HOME/.config}/qt5ct/colors/Akyuu.conf"
QT_QPA_PLATFORMTHEME=qt5ct qt5ct
```

In **Appearance**, choose **Fusion**, enable the custom color scheme and select
**Akyuu**. Breeze also works if its Qt 5 widget style is installed. Apply the settings.

Launch a Qt 5 application with the same platform theme:

```sh
QT_QPA_PLATFORMTHEME=qt5ct application
```

Replace `application` with the application's command.

## Qt 6 with qt6ct

Install qt6ct, then copy the palette:

```sh
install -Dm644 qt6ct/Akyuu.conf "${XDG_CONFIG_HOME:-$HOME/.config}/qt6ct/colors/Akyuu.conf"
QT_QPA_PLATFORMTHEME=qt6ct qt6ct
```

In **Appearance**, choose **Fusion**, enable the custom color scheme and select
**Akyuu**. Breeze also works if its Qt 6 widget style is installed. Apply the settings.

Launch a Qt 6 application with:

```sh
QT_QPA_PLATFORMTHEME=qt6ct application
```

For a persistent setting, use your desktop session's environment configuration.
Use the platform theme supported by your installed Qt version. Some qt6ct builds
also accept `qt5ct` as an alias; the commands above use the explicit names.
Setting the variable twice does not configure both versions: the last value wins.
Plasma users should normally keep Plasma's native integration.

## Remove

Select another scheme first, then remove the installed files:

```sh
rm "${XDG_DATA_HOME:-$HOME/.local/share}/color-schemes/Akyuu.colors"
rm "${XDG_CONFIG_HOME:-$HOME/.config}/qt5ct/colors/Akyuu.conf"
rm "${XDG_CONFIG_HOME:-$HOME/.config}/qt6ct/colors/Akyuu.conf"
```

Remove only the files you installed. Reopen applications to refresh their styles.

References: [KDE color schemes](https://docs.kde.org/stable_kf6/en/plasma-workspace/kcontrol/colors/),
[Qt platform-theme option](https://doc.qt.io/qt-6/qguiapplication.html#supported-command-line-options).
