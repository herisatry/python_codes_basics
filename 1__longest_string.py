# Python3 code to demonstrate working of 
# Longest String in list 
# using max() + key 

def max_str(liste):    
    # Longest String in list 
    # using max() + key 
    res = max(test_list, key = len)
    return res

# initialize list  
test_list = ['gfg', 'is', 'best', 'for', 'geeks']

# printing original list  
print("The original list : " + str(test_list)) 
  
# printing result 
print("Maximum length string is : " + max_str(test_list))