import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import sys

class ChangeHandler(FileSystemEventHandler):
    """Restart the game when a file change is detected."""
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command)

    def on_any_event(self, event):
        if event.is_directory:
            return None

        if self.process:
            self.process.kill()
        self.process = subprocess.Popen(self.command)

if __name__ == "__main__":
    path = '.'  # The directory to watch
    command = ['python3', 'game.py']  # Command to run your game

    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
