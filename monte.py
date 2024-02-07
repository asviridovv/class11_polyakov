from random import random
from math import *
N = 1000000
M = 0

for i in range(N):
    x = random()
    y = random()
    if x * x + y * y <= 1:
        M += 1
er = abs(4*M/N - pi) / pi * 100
print(f"Значение Pi = {4*M/N}")
print(f"Ошибка = {er}")