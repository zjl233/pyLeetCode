from typing import Callable
from threading import Condition, Thread, Condition, Lock


class Foo:
    def __init__(self):
        self.lock1 = Lock()
        self.lock2 = Lock()

        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.

        with self.lock1:
            printSecond()
            self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.

        with self.lock2:
            printThird()


if __name__ == '__main__':
    foo = Foo()
    t1 = Thread(target=foo.first, args=(lambda: print('first'),))
    t2 = Thread(target=foo.second, args=(lambda: print('second'),))
    t3 = Thread(target=foo.third, args=(lambda: print('third'),))

    t2.start()
    t1.start()

    t3.start()

    t1.join()
    t2.join()
    t3.join()
