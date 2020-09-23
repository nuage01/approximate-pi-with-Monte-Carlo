# Monte carlo Pi
from math import sqrt
from random import random
from joblib import Parallel, delayed
from joblib import parallel_backend
import multiprocessing
from multiprocessing import Pool
import csv

opt = [5000, 5000, 10000]
N = 1000000
global COMPTEUR
COMPTEUR = 0
def calcul(N,COMPTEUR, **args):
    for i in range(N):
        x = random()
        y = random()
        r = sqrt(x**2+y**2)
        if r <= 1:
            COMPTEUR = COMPTEUR + 1
    return COMPTEUR

def calcul2(n):
    count = 0
    for i in range(n):
        x = random()
        y = random()
        r = sqrt(x**2+y**2)
        if r <= 1:
            count=count+1
    return count

with parallel_backend('threading', n_jobs=2):
   result = Parallel()(delayed(calcul)(N,COMPTEUR) for N in opt)



if __name__ == "__main__":

    with open('results.csv', mode='w') as results:
        results_write = csv.writer(results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        results_write.writerow(["pi_joblib", "pi_multiprocesing" ])
        for n in range(20):
            calculated = sum(result)
            Pi = 4 * calculated / sum(opt)
            print("calcul pi avec joblib", Pi)
            np = multiprocessing.cpu_count()
            print ('You have {0:1d} CPUs'.format(np))
            part_count=[int(N/np) for i in range(np)]
            pool = Pool(processes=np)
            count = pool.map(calcul2, part_count)
            Pi2= sum(count)/(N*1.0)*4
            print ("calcul de Pi avec multiprocesing:: ", Pi2) 
            results_write.writerow([Pi, Pi2 ])
