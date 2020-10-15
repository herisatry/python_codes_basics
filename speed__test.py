import timeit

# indice3

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


#indice2

# programme qui retourne
# tous les index d'un element dans une liste
def AllIndexesRecursive(input, x, start):

	# si l'index de depart atteint
    # la longueur de la liste,
    # alors on retourne une liste vide

	if (start == len(input)):
		ans = [] # liste vide
		return ans

	# Obtenir la reponse recursive dans
	# la liste smallIndex
	smallIndex = AllIndexesRecursive(input, x, start + 1)

	# If the element at start index is equal
    # Si l'element au depart est egale a x alors

	if (input[start] == x):
		myAns = [0 for i in range(len(smallIndex) + 1)]

		# mettre l'index au debut de la liste
		myAns[0] = start
		for i in range(len(smallIndex)):

			# decalle l'element d'un pas
            # sur la droite et le place
            # dans la liste myAns

			myAns[i + 1] = smallIndex[i]

		return myAns
	else:

		# Si l'element de depart n'est
        # pas egal a x alors on retourne juste la reponse venant de la recursion
		return smallIndex

# Fonction qui determines tous les indices de x dans la liste
def AllIndexes(input, x):

	return AllIndexesRecursive(input, x, 0)



#indice1

def el_index(maListe,mesElements):

	'''
	recherche de l'element item dans la liste mylist
	syntaxe : el_index(list_name,element_researched)
	'''
    
    try:
        #recherche de l'element item dans la liste maliste
        index = maListe.index(mesElements)
        res = ('The index of', mesElements, 'in the list is:', index)
#Dans le cas ou l'element rechercher ne fait pas partie de la liste,
#on utilise un error handler.

    except ValueError:
	    res ='None'
    return res




#test-drive


maListe = [21, 5, 8, 52, 21, 87, 52]
e = 52
# a la place de 52 on peut tester un autre chiffre
# l'index retournee sera 6 , 
#l'index du second 52, si il y en avait un 3ieme alors nous aurions celui du troisieme
#pourquoi? 

print('test index iteratif Q4')
print(timeit.timeit('iterative_ind(maListe,e)',globals=globals()))
print('test index recursif Q3')
print(timeit.timeit('fAllIndexes(maListe,e)',globals=globals()))
print('test index Q2')
print(timeit.timeit('el_index(maListe,e)',globals=globals()))




