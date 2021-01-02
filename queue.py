# inspired from https://www.bogotobogo.com/python/Multithread/python_multithreading_Synchronization_Producer_Consumer_using_Queue.php
import threading
import time
import random
import queue

q = queue.Queue()


class ProducerThread(threading.Thread):
    def __init__(self, target=None, name=None):
        super(ProducerThread, self).__init__()
        self.target = target
        self.name = name

    def run(self):
        while True:
            item = random.randint(1, 10)
            q.put(item)
            print("+ item " + str(item))
            time.sleep(2)
        return


class ConsumerThread(threading.Thread):
    def __init__(self, target=None, name=None, pool_size=10):
        super(ConsumerThread, self).__init__()
        self.target = target
        self.name = name
        self.pool_size = pool_size
        return

    def run(self):
        while True:
            time.sleep(3)
            if not q.qsize() >= self.pool_size:
                elems = []
                for i in range(0, self.pool_size):
                    elems.append(q.get())
                print("- items " + str(elems))
        return


if __name__ == '__main__':
    p = ProducerThread(name='producer')
    c = ConsumerThread(name='consumer')

    p.start()
    c.start()