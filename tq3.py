import random
from time import sleep
from multibar import TqdmBar

# how about putting this one into the classes?

# class WishlistBar(TqdmBar):
#
#     def __init__(self, number):
#         self.total = random.randint(100, 1000)
#         self.items = range(self.total)
#         self.desc = 'Thank you for asking {}'.format(number)
#
#     def process_item(self, item):
#         sleep(random.random() * 0.01)
#
#
# WishlistBar('1').run()

# Since I am no longer using this example on presentations,
# to all vigilant people who noticed tq3 missing from my talk...

print('Good catch! :-)')
