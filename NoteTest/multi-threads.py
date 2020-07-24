from NoteTest.download import get_links, setup_download_dir, download_link
from threading import Thread
import os
from queue import Queue
import logging
from time import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

os.environ["IMGUR_CLIENT_ID"] = "546c25a59c58ad7"


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            download_dir, link = self.queue.get()
            try:
                download_link(download_dir, link)
            finally:
                self.queue.task_done()


def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    queue = Queue()
    for n in range(6):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()

    for link in links:
        logging.info('%s %s', download_dir, link)
        queue.put((download_dir, link))

    queue.join()

    logging.info("Took %s", time() - ts)


if __name__ == '__main__':
    main()
