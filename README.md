# ccseer-nefpreview
NEF (Nikon Electronic Format) Previewer for Seer

## Build Requirements
* Python 2.7 or 3.4
* [rawpy](https://pypi.python.org/pypi/rawpy) (NEF processing)
* [numpy](https://pypi.python.org/pypi/numpy) (Required for rawpy)
* [imageio](https://pypi.python.org/pypi/imageio) (NEF to JPG conversion)
* [pyinstaller](https://pypi.python.org/pypi/PyInstaller/) (Other binary packagers may also work)

## Build Instructions
* Create a portable binary:

    C:\Python34\Scripts\pyinstaller.exe nef2jpeg.py

* Copy `plugin.json` to `dist\nef2jpeg\`

## Installation Instructions
* Go to the `Plugins` section in Seer's `Settings` dialog.
* Select the `Local` tab.
* Click the `Add` button and select the `plugin.json` file.
