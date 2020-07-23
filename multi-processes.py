from download import get_links, setup_download_dir, download_link
from functools import partial
import os
import logging
from time import time
from multiprocessing import Pool

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

os.environ["IMGUR_CLIENT_ID"] = "546c25a59c58ad7"


def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    links = get_links(client_id)
    download_dir = setup_download_dir()
    download = partial(download_link, download_dir)
    with Pool(12) as p:
        p.map(download, links)
    logging.info('Took %s seconds', time() - ts)


if __name__ == '__main__':
    main()
