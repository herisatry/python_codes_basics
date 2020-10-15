#element test 

liste = [21, 5, 8, 52, 21, 87, 52]
elements = 52


#definition de la fonction

def el_index(maListe,mesElements):
	'''
	recherche de l'element item dans la liste mylist
	syntaxe : el_index(list_name,element_researched)
	
	'''
    try:
        #recherche de l'element item dans la liste maliste
        index = maListe.index(mesElements)
        res = ('indice de ', mesElements, 'dans la liste est : ', index)
	
#Dans le cas ou l'element rechercher ne fait pas partie de la liste, 
#on utilise un error handler.

    except ValueError:
	    res ='None'
    return res

print(el_index(maliste,elements))
