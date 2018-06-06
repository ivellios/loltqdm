import multiprocessing
import signal
import random

from tqdm import tqdm
from time import sleep

from multibar import TqdmBar


class MultiBar:
    tqdm = tqdm

    def __init__(self, tqdmprocess_list, threads, total=None, desc='Actions'):
        self.list = tqdmprocess_list
        self.total = total
        self.threads = threads
        self.desc = desc

    def worker_wrapper(self, arg):
        args, kwargs = arg
        return self.worker(*args, **kwargs)

    def run(self):
            original_sigint_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)
            pool = multiprocessing.Pool(processes=self.threads)
            signal.signal(signal.SIGINT, original_sigint_handler)

            try:
                pool_generator = pool.imap_unordered(self.worker, self.list)
                for response in self.tqdm(pool_generator,
                                          total=self.total,
                                          desc=self.desc, position=0):
                    pass
            except KeyboardInterrupt:
                pool.terminate()
            else:
                pool.close()
            pool.join()

    def worker(self, group_item):
        current = multiprocessing.current_process()
        position = current._identity[0]

        group_item.run(position=position)


# ##### Example time


class WishlistBar(TqdmBar):

    def __init__(self, number):
        self.total = random.randint(100, 1000)
        self.items = range(self.total)
        self.desc = 'Wishlist {}'.format(number)

    def process_item(self, item):
        sleep(random.random() * 0.01)


wishlists = [
    WishlistBar(i) for i in range(1000)
]

m = MultiBar(wishlists,
             20,
             total=len(wishlists),
             desc='Super Duper Ultra Progressbar | Wishlists')
m.run()
