#py4e lists lesson
#algorithms - a set of rules used to solve a problem
#Data structures - a particular way of organizing data in a computer
#what is NOT a collection -- 
#a variable has one value which is overwritten - cant have more than one value in a variable
#A list is kinda like a collection -- allows us to put many values into a single variable
# designated by square brackets []

print (['red', 'blue', 24, [5, 6], 'banana'])

friends = ['John','Joe','Bob']
for friend in friends:            #friend is the iterative varivable of the list friends
    print ('whats up,', friend, '?' )

print('BREAK')

x = ['John','Joe','Bob']
for y in x:            #this proves it
    print ('whats up,', y, '?' )

#you can pick out positions from a list just like strings -- they are zero based ie

print(' ')

friends = ['John','Joe','Bob']
print (friends[1])

print(' ')
#unlike strings, lists are mutable -- the OG string can be edited 

lotto = [7, 13, 17, 23, 27]
print (lotto)
lotto[2] = 93
print (lotto)

print(' ')

#range function -- returns a list of numbers that range from zero to one less than the parameter
#we can construct an index loop using for and an integer iterator

print (range(4))
friends = ['John','Joe','Bob']

print(len(friends))

print(range(len(friends)))

print(' ')
#maybe a better example prints the pos of every number out up to but not including 6

x = range(6)

for n in x:
  print(n)
  
print(' ')
#range can incriment by 1 (default) or by another integer if specified 

x = range(3, 20, 2) #the third number after the last comma is what the list will iterate by
for n in x:
  print(n)

print(' ')
#this range function makes for more sofisticated loops

friends = ['John','Joe','Bob']
for i in range(len(friends)):            #i is the iterative varivable of the list friends
    friend = friends[i]
    print ('whats up,', friend, '?' )

#######################################################################################################################################################
print(' ')
#concatenating lists using + --- you can create a new list by adding two lists together

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print (c)
print (a)  #doesnt change original variable

print(' ')

#slicing a list

t = [9, 41, 12, 7, 74, 15]
m = t[1:3]
print (m)
l = t[:4]
print (l)
p = t[3:]
print (p)
q = t[:]
print (q)

#there are a few methods attatched to lists 
print(' ')
print(' ')
#building a list from scratch with methods

stuff = list()
stuff.append('book')
stuff.append(99)
print (stuff)
stuff.append('cookie')
print (stuff)
stuff.reverse()
print (stuff)

print(' ')
print(' ')
#little script for finding the average of user inputs that doesn't require all the loops

#numlist = list()
#while True:
    #inp = input('Enter a number: ')
   #if inp == 'done': break
    #value = float(inp)
    #numlist.append(value)

#average = sum(numlist) / len(numlist)
#print('average is: ', average)

print(' ')
print(' ')

#Split function -- takes strings with spaces and breaks them up into operable lists

abc = 'with three words'
stuff = abc.split()
print(stuff)
stuff.sort()
print(stuff)
print(stuff[0])


print(' ')
print(' ')
#you can choose what the split function is deciding to split the string its based off of.
#split divides strings based on spaces by default but your data set may not have spaces to split on. -- this is called a delimiter
#if it were seperated by semicolons or somthing you could also do that -- example below
line = 'first;second;third'
thing = line.split()
print (thing)
print (len(thing))  #this did nothing and it remained one string object

print(' ')

line = 'first;second;third'
thing = line.split(';') #this deliminates the string via the semicolons and provides and operatable list
print (thing)
print (len(thing))

#you can use this spliting function to split strings multiple times to boil down to what you want. 
#you can chop out all the words by space and then cut those down by @ to get an email domain or something