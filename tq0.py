from time import sleep
import random

items = random.randint(100, 1000)

for x in range(items):
    sleep(random.random() * 0.01)
    print('Element {}'.format(x))
