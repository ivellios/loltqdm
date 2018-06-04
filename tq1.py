from tqdm import tqdm
from time import sleep
import random

items = random.randint(100, 1000)

for x in tqdm(range(items),
              total=items,
              position=0,
              desc='Super Progressbar | Wishlists items',
              unit='awesomeness'):
    sleep(random.random() * 0.01)
