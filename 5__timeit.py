import timeit

'''
la fonction definie retourne une liste de k element,
l'utilisation de timeit permet de calculer le temps d'execution de la fonction f.
temps d'execution : 2.2360258 sec,
globals est un argument optionel qui definit un namespace dans lequel le code est execute.

'''

def f(liste, elem):
    return elem in liste

k=200
ltest = list(range(k))

print(timeit.timeit('f(ltest,k)',globals=globals()))