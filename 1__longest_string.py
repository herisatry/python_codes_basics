# find the longest string , with the help of max() and a key

def max_str(liste):    
    # chaine de caractere la plus longue avec 
    # usage de max() + key 
    res = max(test_list, key = len)
    return res

# list initialization  
test_list = ['test', 'test123', 'test1234', 'tester12345', '1234testing']

# original list  
print("The original list : " + str(test_list)) 
  
# result 
print("La plus longue chaine de caractere est : " + max_str(test_list))
