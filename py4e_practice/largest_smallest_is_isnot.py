#largest number

largest_so_far = -1 #the number determined to be bigger with in the loop is redefined here, above the loop
print('before', largest_so_far)
for the_num in [3, 41, 12, 9, 74, 15]: #you can not change the value of the items in the set within the loop, if you set the_num = largest_so far it just ignores it
    if the_num > largest_so_far: #checking to see if the number in the set is larger than the value currently set for largest_so_far
        largest_so_far = the_num #changing the value for the variable outside of the loop
    print('The largest number so far is',largest_so_far, 'compared to the most recent query of', the_num)
print('after', largest_so_far)
print('Done!')

#smallest number

smallest_so_far = None   #None is its own None type value like a boolean value. Represents an empty space more accurate than -1 or 1000 becuase we might not know whats in the set
print('before', smallest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if smallest_so_far is None: #'is' and 'is not' are also a special word, stronger than an equal sign useful for True/False and Nones
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num 
    print('The smallest number so far is',smallest_so_far, 'compared to the most recent query of', the_num)
print('after', smallest_so_far)
print('Done!')