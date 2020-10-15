import random

def fusion(L1,L2):
    '''
    les differentes liste L1 et L2
    seront chacunes fusionees entre elles deux a deux pour avoir une liste triee.
    ces listes deux a deux seront encore fusionnees entre elle, ainsi de suite jusqu'a 
    obtenir la taille de depart.
    '''
    n1 = len(L1)
    n2 = len(L2)
    L12 = [0]*(n1+n2)
    i1 = 0
    i2 = 0
    i = 0
    while i1<n1 and i2<n2:
        if L1[i1] < L2[i2]:
            L12[i] = L1[i1]
            i1 += 1
        else:
            L12[i] = L2[i2]
            i2 += 1
        i += 1
    if i1<n1:
        while i1<n1:
            L12[i] = L1[i1]
            i1 += 1
            i += 1
    else:
        while i2<n2:
            L12[i] = L2[i2]
            i2 += 1
            i += 1
    return L12

def triFusionRecursif(L):
    '''
    en utilisant la recursion,dans la liste L,
    cette fonction separe la liste L en L1 et L2
    qui les separera encore en plus petite liste
    jusqu'a ce que la longeur des listes separees
    soient inferieure a 1.
    
    '''
    n = len(L)
    if n > 1:
        p = int(n/2)
        L1 = L[0:p]
        L2 = L[p:n]
        print("sepration : ",L1,L2)
        triFusionRecursif(L1)
        triFusionRecursif(L2)
        L[:] = fusion(L1,L2)
        print("fusion : ",L)
    
def triFusion(L):
    '''
    syntaxe : triFusion(liste_name)
    '''
    M = list(L)
    triFusionRecursif(M)
    return M
                  
#creation d'une liste vide 
#avec 11 element qui seront generee par random
#afin de tester notre tri fusion
liste = [] 
for k in range(11):
    liste.append(random.randint(0,20))
print("Liste initiale : ",liste)
orderedList = triFusion(liste)
print(orderedList)
