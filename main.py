import sys
import time

from watchdog.observers import Observer
from configparser import ConfigParser

import handlers

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    def get_config(filename):
        config = ConfigParser(allow_no_value=True)
        config.optionxform = str
        try:
            config.read(filename)
            return config
        except Exception as error:
            print(error)

    config = get_config("config.ini")
    handlers_to_observe = [getattr(handlers, handler_name)() for handler_name in config['HANDLERS']]

    if handlers_to_observe:
        threads = []
        observer = Observer()

        for handler in handlers_to_observe:
            observer.schedule(handler, path=path, recursive=True)
            threads.append(observer)
        observer.start()

        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    
    else:
        print("*** Nothing to observe. Register handlers in config file! ***")