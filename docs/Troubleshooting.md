# Troubleshooting

## The scheme does not appear

Check that the file is in the directory for the correct tool. KDE uses
`color-schemes/Akyuu.colors` under the data directory; qtct uses
`qt5ct/colors/Akyuu.conf` or `qt6ct/colors/Akyuu.conf` under the config directory.
Close and reopen the settings tool after copying the file.

## Colors change only in part of the window

A widget style can draw its own colors. Try Fusion, or Breeze if installed,
and select Akyuu as the custom palette. An application's own theme or stylesheet
may still take precedence over the platform palette.

## Dolphin turns light after choosing Default

Outside Plasma, KDE's color-scheme manager can choose a Breeze fallback when
qtct supplies the platform theme. Copying the KDE scheme alone does not change
that fallback.

Select **Akyuu** explicitly in Dolphin's color-scheme menu. To use Dolphin's
native KDE integration in a separate window, run:

```sh
dolphin -platformtheme kde --new-window
```

This requires KDE's Qt platform-theme plugin, provided by `plasma-integration`
on Arch Linux. Select Akyuu in the new window. The command-line option affects
this Dolphin process; it leaves the environment inherited by child applications
unchanged. `--new-window` avoids reusing an older Dolphin process.

## An application ignores qtct

Check which Qt version it uses and start it with the matching platform theme
from the installation guide. Sandboxed applications may need the palette inside
their sandbox. Applications with independent theme engines need their own themes.

If reporting a problem, include the application, Qt version, platform theme,
widget style and a screenshot. Remove personal information from the image.
