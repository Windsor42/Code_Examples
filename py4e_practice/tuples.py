#tuples are like lists - reductionist versions of lists
#round brace () instead of square brace []
#methods and functions work very much the same
#the difference is that tuples are immutable
#you can not insert, delete, mutate things in a tuple
#the benifit of this is that they are more compact -- they take up less storage, easier to access, ect
#good for temporary variables 
#higher performance

(x, y) = (4, 'fred') #you can make two assignment statements in one - X = 4 and y = fred
print (y)

#this is useful in dictionaries for pulling out ~ key , value ~ pairs

d = dict()
d['corn'] = 2
d['jacob'] = 4              #assigning tags and values 
for (k,v) in d.items():     #iterating through the tags and values and assigning them to k and v
    print(k,v)              # prining those pairs

#below is another way to pull out those assoicaited pairs though, not as prettyAZS
tups = d.items()
print(tups)
# this will print out the associated pairs as well
#tuples are comparable -- when compareing two sets of values it compares them one by one in order until a true or...
#false statement can be made. It also will compare string by string and letter by letter within two strings
#never compares any further than it has to

#######################

#tuples are useful for organizing dictionary items
#convert dictionary to a list --> sort the list --> orgainize

d = {'a':10, 'b':1, 'c':22}
d.items()
print(d.items()) #this dictionary my or may not be sorted in its component tupeles
for k,v in sorted(d.items()): # this is a nice succict way to organiz
    print(k,v)