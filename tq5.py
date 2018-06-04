import random

from multibar import MultiBar, TqdmBar
from time import sleep

from loltqdm import loltqdm


class LolRandomProcessing(TqdmBar):
    tqdm = loltqdm

    def __init__(self, number):
        self.total = random.randint(100, 800)
        self.items = range(self.total)
        self.desc = 'Wishlist {}'.format(number)

    def process_item(self, item):
        sleep(random.random() * 0.01)


class LolMultiTqdm(MultiBar):
    tqdm = loltqdm


randoms = [
    LolRandomProcessing(i) for i in range(1000)
]

m = MultiBar(randoms, 20,
             total=len(randoms),
             desc='Super Duper Turbo Ultra Progressbar | Wishlists')
m.run()
