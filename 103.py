import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

to="C:/Users/SUZANA/Desktop/Projeto101"
fromD="c:/Users/SUZANA/Desktop/Python1"

class FileMovementHandler(FileSystemEventHandler):
 def on_created(self, event): 
  print("A")
  print("Arquivo ",os.path.basename(event.src_path)," foi criado")
 def on_modified(self, event): 
  print("B")
  print("Arquivo ",os.path.basename(event.src_path)," foi modificado")
 def on_moved(self, event): 
  print("C")
  print("Arquivo ",os.path.basename(event.src_path)," foi movido")
 def on_deleted(self, event): 
  print("D")
  print("Arquivo ",os.path.basename(event.src_path)," foi deletado")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, fromD, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()