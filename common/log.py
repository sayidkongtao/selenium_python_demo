import logging
import os

PATH = lambda path: os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        path
    )
)


class LoggerHandler(logging.Logger):

    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 log_format=None
                 ):
        super().__init__(name)

        self.setLevel(level)

        fmt = logging.Formatter(log_format)

        if file:
            file_handler = logging.FileHandler(file, encoding='utf-8', mode="a")
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)


logger = LoggerHandler(file=PATH(os.path.join("..", "log", 'log.log')),
                       log_format="%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s")
