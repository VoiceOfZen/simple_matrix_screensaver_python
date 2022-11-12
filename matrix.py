import os
import time
import random

os.system('color 0a')

nums = [0, 1]
tm = 0

#    1     1      0     1   1      0    0     1     0      0   1      0      1
# (make space + make num * how many numbers) * how many lines


while tm < 30:
    rand = []
    for i in range(30):
        rand += [random.randrange(3,15)* " "] + [str(random.choice(nums))]

    rand = ''.join(rand)
    print(rand)

    tm = tm + 0.1

    time.sleep(0.1)
