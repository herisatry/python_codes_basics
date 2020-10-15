import random

def triInsertion(liste):
    '''
    Tri par insertion : consiste a prendre les elements 
    un par un, dans l’ordre de rangement dans la liste, 
    et a les inserer dans une liste secondaire au bon emplacement.
    syntaxe : triInsertion(liste)
    '''
    L = list(liste) #la liste de type list, on se rassure qu'on a bien une liste
    N = len(L) #longuer de la liste
    for n in range(1,N):
        cle_ = L[n] 
        j = n-1 #index de l'element precedent , si n=1 (element numero 2 de la liste), alors j=0 (l'element au tout debut de la liste)
        while j>=0 and L[j] > cle_: #tant que j n'est pas inferieur a zero and que l'element 
            L[j+1] = L[j] # decalage vers la droite de l'element le plus grand, et sur la gauche le plus petit
            j = j-1
        L[j+1] = cle_
    return L
 
 # genere un liste avec 10 elements random, allant entre 0 et 20
liste = []
for k in range(10):
    liste.append(random.randint(0,20))
listeTriee = triInsertion(liste)

#liste sans tri                     
print('Liste avant tri : ',liste)
#liste avec tri
print('Liste apres tri : ',listeTriee)
