import os
import subprocess

from watchdog.events import PatternMatchingEventHandler
from PIL import Image

class HandlerToDeleteJsFile(PatternMatchingEventHandler):
    def __init__(self):
        self._patterns = ['*.js']
        self._ignore_directories = True
        self._case_sensitive = False
        self._ignore_patterns = ['.vscode/*']

    def process(self, event):
        os.remove(event.src_path)
        print("Delete file: {}".format(event.src_path))

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

class HandlerToGrayscaleImage(PatternMatchingEventHandler):
    def __init__(self):
        self._patterns = ['*.jpg', '*.gif']
        self._ignore_directories = True
        self._case_sensitive = False
        self._ignore_patterns = ['.vscode/*']
    
    def process(self, event):
        image = Image.open(event.src_path).convert('LA')
        image.save('{}_grayscale.png'.format(event.src_path))
        print("Grascale image: {}".format(event.src_path))

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)

class HandlerToCompileC(PatternMatchingEventHandler):
    def __init__(self):
        self._patterns = ['*.c']
        self._ignore_directories = True
        self._case_sensitive = False
        self._ignore_patterns = ['.vscode/*']

    def process(self, event):
        cmd = event.src_path
        subprocess.check_call(["gcc", "-o", cmd[:-2]+"_compiled", cmd])
        print("Compile: {}".format(event.src_path))

    def on_created(self, event):
        self.process(event)

    def on_modified(self, event):
        self.process(event)