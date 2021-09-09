import threading
import time


def func1(idthread):
    print('Thread', idthread, 'started')
    time.sleep(5)
    print('Thread', idthread, 'ended')


def func2(idthread):
    print('Thread', idthread, 'started')
    thOne.join()
    print('Thread', idthread, 'ended')


thOne = threading.Thread(target=func1, args=('t1',))
thOne.start()
thTwo = threading.Thread(target=func2, args=('t2',))
thTwo.start()
