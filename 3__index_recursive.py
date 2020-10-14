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
    #  
 
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

# Code test 
arr = [ 1, 2, 3, 2, 2, 5 ] 
x = 2

output=AllIndexes(arr, x) 

print('les indices pour ',x, ' sont ' ,output)

