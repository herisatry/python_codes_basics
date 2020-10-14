maliste = [21, 5, 8, 52, 21, 87, 52]
elements = 52

def el_index(maliste,elements):
    try:
        #recherche de l'element item dans la liste mylist
        index = maliste.index(elements)
        res = ('The index of', elements, 'in the list is:', index)
        
    except ValueError:
	    res ='None'
    return res

print(el_index(maliste,elements))
