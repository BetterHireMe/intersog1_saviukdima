# Filesystem monitoring application
The app monitor the current directory for file system changes and execute certain handlers registered in configuration file. This implementation includes:
* Deleting files with js extension
* Converting colored images to grayscale
* Compiling files with c extension
## Getting Started
Just uncomment the required handlers in ```config.ini``` and run script:
``` ini
[HANDLERS]
#HandlerToDeleteJsFile
#HandlerToGrayscaleImage
#HandlerToCompileC
```

### Requirements
* [Watchdog](https://pythonhosted.org/watchdog/) - Python API library and shell utilities to monitor file system events.
* [Pillow](https://pillow.readthedocs.io/en/stable/) - Pillow is the friendly PIL fork by [Alex Clark and Contributors](https://github.com/python-pillow/Pillow/graphs/contributors). PIL is the Python Imaging Library by Fredrik Lundh and Contributors.
### Installation
Clone this repo and go to the project forlder:
```
git clone https://github.com/saviukdima/filesystem_monitoring_app.git
cd filesystem_monitoring_app
```
Activate virtual environment, install all dependencies and run script:
```
pipenv shell
pipenv sync
python main.py
```