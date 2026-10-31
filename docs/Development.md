# Regenerating the Qt palettes

`Akyuu.colors` is the source for the files in `qt5ct/` and `qt6ct/`.
The exporter uses the KDE color-scheme parser to produce active, inactive and
disabled palettes: 21 roles for Qt 5 and 22 for Qt 6.

The exporter needs CMake, Qt 6 Widgets and KDE Frameworks 6 ColorScheme development
files. Users installing the supplied palettes do not need build tools.

```sh
cmake -S . -B build
cmake --build build
QT_QPA_PLATFORM=offscreen ./build/export-qt-palettes Akyuu.colors .
```

Update the KDE scheme first, then regenerate both Qt palettes. Keep the explicit
inactive Header group: an inherited light header can make an otherwise dark
application turn white when it loses focus.

The palette was exported and checked with Qt 6.11 and KF6 6.31. The supplied
Qt 5 palette was loaded with Qt 5.15. There is no runtime dependency between
this repository and the Akyuu application.

To refresh the widget preview, install PySide6 6.6 or newer and run:

```sh
python3 tools/preview.py
```

The preview uses the generated Qt 6 palette and writes `images/akyuu.png`.
