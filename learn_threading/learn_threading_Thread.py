# -*- encoding: utf-8 -*-
import threading
import time


def t1(t2):
    print 'now in t1'
    t2.start()
    t2.join()
    print 'out t1'


def t2():
    print "now in t2"
    time.sleep(1)
    print "out t2"


if __name__ == '__main__':
    t2_obj = threading.Thread(target=t2)
    t1_obj = threading.Thread(target=t1, args=(t2_obj, ))

    t1_obj.start()