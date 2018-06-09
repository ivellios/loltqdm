import random
from time import sleep

from tqdm import tqdm

wishlists = random.randint(10, 20)

for i in tqdm(range(wishlists), desc='Super Duper Progressbar | Processing Wishlists', unit='wishlists', leave=False,):
    items = random.randint(20, 300)
    for j in tqdm(range(items),
                  desc='Items on wishlist {}'.format(i),
                  ascii=True,
                  position=1):
            sleep(random.random() * 0.01)
