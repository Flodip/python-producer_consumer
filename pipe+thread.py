from multiprocessing import Pipe
import threading
import time


def _th_receive(c, previous_th=None):
    if previous_th is not None:
        # waiting for previous receive to end
        previous_th.join()
    print(c.recv())


def _th_send(p, msg):
    # print(time.time())
    p.send(msg)


def consumer(c, sleep_time):
    th = threading.Thread(target=_th_receive, args=(c,))
    th.start()
    while True:
        time.sleep(sleep_time)
        th = threading.Thread(target=_th_receive, args=(c, th,))
        th.start()


def producer(p, sleep_time):
    # feeding a message every time seconds
    i = 0
    while True:
        time.sleep(sleep_time)
        t = threading.Thread(target=_th_send, args=(p,"message" + str(i)))
        t.start()
        t.join()
        i += 1


p, c = Pipe()
th = threading.Thread(target=consumer, args=(c, 3))
th.start()
producer(p, 2)