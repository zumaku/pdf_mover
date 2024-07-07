import time
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

class PDFHandler(FileSystemEventHandler):
    def __init__(self, source_folder, destination_folder):
        self.source_folder = source_folder
        self.destination_folder = destination_folder

    def on_modified(self, event):
        for filename in os.listdir(self.source_folder):
            if filename.endswith('.pdf'):
                src = os.path.join(self.source_folder, filename)
                now = datetime.now().strftime('%Y%m%d_%H%M%S')
                new_filename = f'{now}_{filename}'
                dst = os.path.join(self.destination_folder, new_filename)
                shutil.move(src, dst)
                print(f'Moved at {now}: {new_filename}')

if __name__ == "__main__":
    source_folder = 'C:\\Users\\FADLI\\Downloads'
    destination_folder = 'D:\\Kuliah\\OTW SKRIPSI\\Proposal\\References'

    # Print startup message with timestamp
    startup_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Program started at {startup_time}\nWathing PDF file to move on {source_folder}')

    event_handler = PDFHandler(source_folder, destination_folder)
    observer = Observer()
    observer.schedule(event_handler, path=source_folder, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

