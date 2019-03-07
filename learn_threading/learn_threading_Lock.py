# -*- encoding: utf-8 -*-
import threading
import time


data = 0
lock = threading.Lock()


def func(i):
    global data
    threading.currentThread().setName("t"+str(i))
    print '%s acquire lock...' % threading.currentThread().getName()

    if lock.acquire():
        print '%s get the lock...' % threading.currentThread().getName()
        data += 1
        print data
        time.sleep(2)
        print '%s release lock...' % threading.currentThread().getName()
        lock.release()


if __name__ == "__main__":
    t1 = threading.Thread(target=func, args=(1, ))
    t2 = threading.Thread(target=func, args=(2, ))
    t3 = threading.Thread(target=func, args=(3, ))

    t1.start()
    t2.start()
    t3.start()