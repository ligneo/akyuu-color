#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 cenky <cenkkgl@gmail.com>
# SPDX-License-Identifier: GPL-3.0-or-later

import os
from pathlib import Path

os.environ["QT_QPA_PLATFORM"] = "offscreen"
os.environ["QT_SCALE_FACTOR"] = "1"

from PySide6.QtCore import QSettings, Qt
from PySide6.QtGui import QColor, QFont, QPalette
from PySide6.QtWidgets import (
    QApplication, QCheckBox, QComboBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QTableWidget, QTableWidgetItem, QTabWidget, QVBoxLayout, QWidget,
)

root = Path(__file__).resolve().parent.parent
app = QApplication([])
app.setStyle("Fusion")
app.setFont(QFont("Noto Sans", 11))
settings = QSettings(str(root / "qt6ct/Akyuu.conf"), QSettings.IniFormat)
palette = QPalette()
for group, key in ((QPalette.Active, "active_colors"),
                   (QPalette.Inactive, "inactive_colors"),
                   (QPalette.Disabled, "disabled_colors")):
    for role, color in enumerate(settings.value("ColorScheme/" + key)):
        palette.setColor(group, QPalette.ColorRole(role), QColor(color))
app.setPalette(palette)

window = QMainWindow()
window.setWindowTitle("Akyuu")
for title in ("File", "Edit", "View", "Help"):
    window.menuBar().addMenu(title)
container = QWidget()
window.setCentralWidget(container)
layout = QHBoxLayout(container)
sidebar = QListWidget()
sidebar.addItems(["Overview", "Library", "Downloads", "Archive"])
sidebar.setCurrentRow(1)
sidebar.setFixedWidth(150)
layout.addWidget(sidebar)
tabs = QTabWidget()
layout.addWidget(tabs)
page = QWidget()
tabs.addTab(page, "Library")
tabs.addTab(QWidget(), "Settings")
body = QVBoxLayout(page)
search = QLineEdit()
search.setPlaceholderText("Filter items")
body.addWidget(search)
table = QTableWidget(4, 3)
table.setHorizontalHeaderLabels(["Name", "Status", "Updated"])
rows = [("Reading list", "In progress", "Today"),
        ("Notes", "Saved", "Yesterday"),
        ("Reference", "Saved", "Yesterday"),
        ("Sketches", "Archived", "Last week")]
for row, values in enumerate(rows):
    for column, value in enumerate(values):
        table.setItem(row, column, QTableWidgetItem(value))
table.horizontalHeader().setStretchLastSection(True)
table.setColumnWidth(0, 245)
table.setColumnWidth(1, 155)
table.setSelectionBehavior(QTableWidget.SelectRows)
table.selectRow(0)
body.addWidget(table)
swatches = QHBoxLayout()
for name, role in (("Window", QPalette.Window), ("View", QPalette.Base),
                   ("Button", QPalette.Button), ("Purple", QPalette.Highlight),
                   ("Lavender", QPalette.Link), ("Amber", QPalette.LinkVisited)):
    cell = QVBoxLayout()
    patch = QFrame()
    patch.setFixedHeight(32)
    color = palette.color(role).name()
    border = palette.color(QPalette.Midlight).name()
    patch.setStyleSheet(f"background: {color}; border: 1px solid {border};")
    cell.addWidget(patch)
    cell.addWidget(QLabel(name))
    swatches.addLayout(cell)
body.addLayout(swatches)
options = QHBoxLayout()
check = QCheckBox("Show previews")
check.setChecked(True)
options.addWidget(check)
radio = QRadioButton("Details")
radio.setChecked(True)
options.addWidget(radio)
combo = QComboBox()
combo.addItems(["All items", "Saved", "Archived"])
options.addWidget(combo)
body.addLayout(options)
progress = QProgressBar()
progress.setValue(65)
body.addWidget(progress)
buttons = QHBoxLayout()
buttons.addStretch()
disabled = QPushButton("Delete")
disabled.setEnabled(False)
buttons.addWidget(disabled)
buttons.addWidget(QPushButton("Cancel"))
save = QPushButton("Save")
save.setDefault(True)
buttons.addWidget(save)
body.addLayout(buttons)
window.statusBar().showMessage("Akyuu · Qt Widgets / Fusion")
window.resize(940, 530)
window.show()
table.setFocus()
app.processEvents()
app.processEvents()
output = root / "images/akyuu.png"
output.parent.mkdir(exist_ok=True)
if not window.grab().save(str(output)):
    raise OSError(f"Could not write {output}")
