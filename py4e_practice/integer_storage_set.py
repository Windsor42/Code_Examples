#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except 
# and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below. 

largest = None
smallest = None

for value in [-1, 12, 22, 42, 69]:

    if smallest is None:
        smallest = value
        largest = value

    if smallest > value:
        smallest = value
           
    if largest < value:
        largest = value


print("Maximum is", largest)
print("Minimum is", smallest)




#Invalid input
#Maximum is 10
#Minimum is 2