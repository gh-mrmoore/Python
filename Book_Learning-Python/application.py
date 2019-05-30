from random import random, sample

num = random()
print('Random Float 0.0-1.0:', num)

num = int(num*10)

nums = []
i = 0

while i < 6:
    nums.append(int(random() * 10) + 1)
    i += 1
print('Random Multiple Integers 1-10:', nums)

nums = sample(range(1, 49), 6)
print('Random Ineger Sample 1-49:', nums)