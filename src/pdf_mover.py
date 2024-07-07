import time
import shutil
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import configparser

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
                print(f'File {new_filename} telah dipindahkan pada {now}')

def greating():
    gretaing = """
 ___ ___  ___   __  __  _____   _____ ___ 
| _ \   \| __| |  \/  |/ _ \ \ / / __| _ \\
|  _/ |) | _|  | |\/| | (_) \ V /| _||   /
|_| |___/|_|   |_|  |_|\___/ \_/ |___|_|_\\
                                        
Sebuah program yang dapat membantumu mengumpulkan referensi!
Dibuat oleh Zumaku.

Dokumentasi => https://github.com/zumaku/pdf_mover
============================================================
"""
    print(gretaing)
    print("[Menjalankan PDF Mover]")

if __name__ == "__main__":
    greating()

    config = configparser.ConfigParser()
    config.read('config.ini')

    source_folder = config['Paths']['source_folder']
    destination_folder = config['Paths']['destination_folder']

    # Print startup message with timestamp
    startup_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'Program berjalan pada saat {startup_time}')
    print(f'Folder Asal: {source_folder}')
    print(f'Folder Tujuan: {destination_folder}')

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
