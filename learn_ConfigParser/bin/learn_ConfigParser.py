# -*- encoding: utf-8 -*-
from ConfigParser import ConfigParser


def main():
    CONFIGFILE = "./conf/config.txt"
    cf = ConfigParser()
    cf.read(CONFIGFILE)

    host = cf.get("server", "host")
    print host

    port = cf.getint("server", "port")
    print port

    cf.set("server", "thread", 200)
    cf.write(open(CONFIGFILE, "w"))

    cf.add_section("people")
    cf.set("people", "girl", "yes")
    cf.set("people", "boy", "yes")
    cf.write(open(CONFIGFILE, "w"))

if __name__ == "__main__":
    main()