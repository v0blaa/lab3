from contextlib import contextmanager
import time

class cm_timer_2:

    def __enter__(self):
        self.time1 = time.time()

    def __exit__(self, *args):
        print('2 таймер: ', time.time() - self.time1)

class cm_timer_1:
    def __enter__(self):
        self.time1 = time.time()
    def __exit__(self):
        print('1 таймер: ', time.time() - self.time1)

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(1.5)
    with cm_timer_2():
        time.sleep(1.5)