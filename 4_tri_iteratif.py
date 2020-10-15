def iterative_ind(maListe,els):
    '''
    syntaxe : iterative_ind(maListe,els)
    en passant par une boucle on obtient l'index de l'element recherche
    '''


    L = list(maListe) #la liste de type list, on se rassure qu'on a bien une liste
    el = mesElements
    N = len(L) #longuer de la liste
    res=[]
    for n in range(0,N):
        if (L[n] == el ):
            res = n
        else :
            res ='None'
    return res


#test-drive


maListe = [21, 5, 8, 52, 21, 87, 52]
mesElements = 52  
# a la place de 52 on peut tester un autre chiffre
# l'index retournee sera 6 , 
#l'index du second 52, si il y en avait un 3ieme alors nous aurions celui du troisieme
#pourquoi? 


print(iterative_ind(maListe,mesElements))



