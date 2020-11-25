import logging

from pynput.keyboard import Listener

from common import log

log.replace_logging_root()


def on_press(key):
    logging.debug(f'on_press: {key}')


def on_release(key):
    logging.debug(f'on_release: {key}')


if __name__ == '__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        logging.debug(f'dog stared')
        listener.join()
