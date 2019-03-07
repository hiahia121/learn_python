# -*- encoding: utf-8 -*-
import urlparse


def divide_url():
    parse_url = urlparse.urlparse("http://www.google.com/search?hl"
                                  "=en&q=urlparse&btnG=Google+Search")
    print parse_url


def pack_url():
    url_scheme = "http"
    url_location = "www.baidu.com"
    url_path = "lib/tuku.com"

    unparse_url = urlparse.urlunparse((url_scheme, url_location, url_path, "", "", ""))

    print unparse_url


if __name__ == "__main__":
    divide_url()
    pack_url()