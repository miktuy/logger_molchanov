import logging


logging.basicConfig()


app_logger = logging.getLogger('app_logger')
console_handler = logging.StreamHandler()
app_logger.addHandler(console_handler)

f = logging.Formatter(fmt='%(levelname)s - %(name)s - %(message)s')
console_handler.setFormatter(f)


utils_logger = logging.getLogger('app_logger.utils')
utils_logger.setLevel("DEBUG")
# utils_logger.propagate = False


def main():
    utils_logger.debug("Hello world")


if __name__ == '__main__':
    main()