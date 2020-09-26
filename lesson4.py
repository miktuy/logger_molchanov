import logging.config

from settings import logger_config


logging.config.dictConfig(logger_config)
logger = logging.getLogger("app_logger")
# logger.setLevel("DEBUG")
#
# std_format = logging.Formatter(fmt="{asctime} - {levelname} - {name} - {message}", style="{")
#
# console_handler = logging.StreamHandler()
# logger.addHandler(console_handler)
# console_handler.setFormatter(std_format)
#
# file_handler = logging.FileHandler("debug.log")
# logger.addHandler(file_handler)
# file_handler.setFormatter(std_format)
words = ["new house", "apple", "ice cream", 3]


def main():
    for item in words:
        try:
            print(item.split(" "))
        except:
            logger.exception(f"Exception here, item={item}")
            pass


if __name__ == '__main__':
    main()
