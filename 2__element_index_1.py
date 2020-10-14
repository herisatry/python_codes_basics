mylist = [21, 5, 8, 52, 21, 87, 52]
item = 52

def el_index(liste,items):
    try:
        #search for the item
        index = liste.index(items)
        res = ('The index of', items, 'in the list is:', index)
        
    except ValueError:
	    res ='None'
    return res

print(el_index(mylist,item))