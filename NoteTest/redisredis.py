import logging
from NoteTest.download import setup_download_dir, download_link, get_links
import os
from rq import Queue
from redis import Redis
from time import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

os.environ["IMGUR_CLIENT_ID"] = "546c25a59c58ad7"


def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    q = Queue(connection=Redis(host='127.0.0.1', port=6379))
    for link in links:
        q.enqueue(download_link, download_dir, link)
    logger.info("Took %s seconds.", time() - ts)


if __name__ == '__main__':
    main()
