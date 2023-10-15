import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Каталоги для отслеживания
directories_to_watch = ['E:\pythonFiles']

# Настройка логирования
logging.basicConfig(filename='file_changes.log', level=logging.INFO)


class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        logging.info(f'File modified: {event.src_path}')

    def on_created(self, event):
        logging.info(f'File created: {event.src_path}')


if __name__ == "__main__":
    event_handler = FileChangeHandler()

    # Создаем наблюдателя
    observer = Observer()
    for directory in directories_to_watch:
        observer.schedule(event_handler, path=directory, recursive=True)

    logging.info("Starting to watch directories...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
