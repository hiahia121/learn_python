# -*- encoding: utf-8 -*-
import logging


def set_log_config():
    cur_file_name = __file__.split('/')[-1].split('.')[0]
    logging.basicConfig(
        #filename="%s.log" % cur_file_name,
        format="[%s(asctime)s][%(levelname)s][%(funcName)s][line:%(lineno)d]:%(message)s",
        level=logging.DEBUG,
        filemode="w"
    )


def main():
    logging.debug("hahaha")


if __name__ == "__main__":
    set_log_config()
    main()