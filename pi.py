# Monte carlo Pi
from math import sqrt
from random import random
from joblib import Parallel, delayed
from joblib import parallel_backend
opt = [5000, 5000, 10000]
global COMPTEUR
COMPTEUR = 0
def calcul(N,COMPTEUR):
    for i in range(N):
        x = random()
        y = random()
        r = sqrt(x**2+y**2)
        if r <= 1:
            COMPTEUR = COMPTEUR + 1
    return COMPTEUR
with parallel_backend('threading', n_jobs=2):
   result = Parallel()(delayed(calcul)(N,COMPTEUR) for N in opt)

calculated = sum(result)
Pi = 4 * calculated / sum(opt)
print(Pi)