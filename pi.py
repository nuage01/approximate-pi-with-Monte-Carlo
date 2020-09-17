# Monte carlo Pi
from math import sqrt
from random import random
from joblib import Parallel, delayed
from joblib import parallel_backend
N = 10000000
compteur = 0

for i in range(N):
    x = random()
    y = random()
    r = sqrt(x**2+y**2)
    if r <= 1:
        compteur = compteur + 1

Pi = 4 * compteur / N
print(Pi)