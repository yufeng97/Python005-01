import os
import logging
from datetime import datetime
from pathlib import Path


def log():
    now = datetime.now()
    date = datetime.strftime(now, "%Y-%m-%d")
    dirpath = f'/var/log/python-{date}'
    if not Path(dirpath).exists():
        os.makedirs(dirpath)
    filename = os.path.join(dirpath, 'geekbang.log')
    logging.basicConfig(filename=filename, 
                        level=logging.INFO, 
                        datefmt="%Y-%m-%d %x", 
                        format="%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s")
    logging.info("test info message")


if __name__ == "__main__":
    log()
