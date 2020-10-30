def SetConvert(string): 
    """
    syntaxe : SetConvert(String)
    la fonction divise une chaine de caractere en liste de caractere trier et sans duplicat de caractere. 
    """
    GeneratedList=[]  #initialisation de la variable qui contiendra la liste
    GeneratedList[:0]=string #decoupage de la chaine de caractere pour en faire une liste 
    #SortedList = sorted(GeneratedList, key=None, reverse=False) # etant donner que un set et immutable , nous commencons par trier la liste
    UniqueName = set(GeneratedList) # afin de garder qu'une liste sans repetitions de caractere , on transforme la liste en sets
    return sorted(UniqueName, key=None, reverse=False)

def DictFreq(string):
    #initialisation de la variable qui contiendra la liste
    GeneratedList=[]  
    MonDico = {}
    #decoupage de la chaine de caractere pour en faire une liste
    GeneratedList[:0]=string
    # nous allons iterer dans la liste et compter la frequence de chaque caractere.
    for el in GeneratedList:
        freq_el = el
        # si l'element de la liste se repete on rajouter plus un a la valeur correspondant a la cle
        if freq_el in MonDico :
            MonDico[freq_el] +=1
        # si l'element de la liste ne se repete pas la valeur correpondant a la cle sera egale a 1
        else :
            MonDico[freq_el] = 1
    return MonDico






# Driver code 

str1="BONJOUR"

charlist = SetConvert(str1)
charDico = DictFreq(str1)


print('la liste unique est : ',charlist)

print('la frequence de chaque caractere est : ',charDico)