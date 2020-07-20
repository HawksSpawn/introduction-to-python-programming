verse = ("if you can keep your head when all about you are losing theirs and blaming it on you\n"   
         "if you can trust yourself when all men doubt you\n"     
         "but make allowance for their doubting too\n"   
         "if you can wait and not be tired by waiting\n"      
         "or being lied about\n"  
         "don’t deal in lies\n"   
         "or being hated\n"  
         "don’t give way to hating\n"      
         "and yet don’t look too good\n"  
         "nor talk too wise\n")
         
print(verse, '\n')

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')
