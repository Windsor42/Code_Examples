fruit = 'banana'
x = fruit[1]   #The first position in the string is registered as 0 so searching for character 1 will give us 'a' 
print(x)       #printing position 1 of defined variable 'fruit' 

#can not index past the end of a string so if I asked for position 10 it would give me an error

###

fruit = 'banana'
x = len(fruit)      #len is a function that tells you the length of the string
print(x)            #we pass a parameter into the function 'len'

####
#you can loop through strings as well

fruit = 'banana'
index = 0 

while index < len(fruit):
    letter = fruit[index]
    print (letter, index)
    index = index + 1

#####
#a defininte loop using a for statement is much more elegant

fruit = 'banana 1234'

for letter in fruit:   #the iteration is taken care of with the iteration variable 'letter' this is not a function just a variable you put in
    print(letter)      #prints all characters iterativly
#the iteration variable iterates through the sequence
#the block body of the code is executed once for each value in the sequence
#the iteration variable moves through each variable in the sequence

### slicing astring
s = 'monty python'
print (s[0:4]) #always means up to but not including
print (s[6:20]) #pythong doesnt care if you blow past the end of the string when slicing it 

#you can concatinate a string by simply adding it together

#the 'in' function in strings can search for a part of a string and return true/false

fruit = 'banana'
if 'a' in fruit:
    print('Found it!')

#string objects have built in capabilities
# .lower() or .swapcase() does not alter the string. the string is passed into it and a new string with all lowercase characters is printed

greet = 'Hello Bob!'
zap = greet.swapcase()
print (zap)

#finding stuff in a string
#finds the first occurance in the string

fruit = 'banana'
pos = fruit.find('na')
print (pos)

#.replace() works like a serach and replace in a word processer ('original', 'what you want to relace it with')
greet = 'Howdy friend!'
ngreet = greet.replace('friend', 'partner')
print(ngreet)

#stripping white space
# lstrip() rstrip() and strip()
# strip white space from the left, right, and both (respectivly)

greet = '     Howdy World!     '
print (greet.lstrip())
print (greet.rstrip())
print (greet.strip())

#prefixes
#.startswith() can tell you (T/F) if a string starts with the input variable

name = input('What is your title?: ')
if name.startswith('Mrs.'):
    print ('Yes')
else:
    print ('No')

#parsing and extracting - you can parse through and cut information out of a string using a technique like the following

data = 'from jacobcommerford@gmail.com'
atpos1 = data.find('@')
print(atpos1)

atpos2 = data.find('.')

whatiwant = data[atpos1+1 : atpos2]
print(whatiwant)

#strings are immutable -- you can not change things inside of a string -- only make a new string with different data