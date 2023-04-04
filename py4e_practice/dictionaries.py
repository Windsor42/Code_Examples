#thing that programmers like the most about python
#sort of like a collection --> you can put multible variables in there
#list is an organized collection #pringles can
#dictionaries are messier - more like a bag of chips - you pull things out based on the key - bag of holding
# refered to as an associative array - there is an association between a key and a value 

purse = dict()
purse['money'] = 12
purse['candy'] = 7
purse['sunglasses'] = 3  #adding somthing to a dictionary does not require a method like the lists 
                         #it is simple added by virtue of assigning a new tag with assigned value to the dictionary

print(purse)
print(purse['candy'])

purse['candy'] = purse['candy'] + 2

print(purse)

#dictionary literals using curly braces to create a dictionary of keys and associated value pairs

jjj = {'chuck': 7, 'diane': 4, 'freddy': 19}
print(jjj)

ooo = { }
print(ooo)

###
#dictionary tracebacks -- dictionaries get mad when you try to invoke a tag that does not exist.
#you can get around this by utilizing the 'in' function -- this is becuase 'in' asks a questions and returns a true or false example below

ccc = dict()
ccc['cowboy'] = 'bannana'
###if I were to use the code below it would blow up on me
#print(ccc['cowboy'])
###so I can use an if instead
if 'cowboy' in ccc:
    print('Yeehaw!')
else:
    print('Yee...naw')

#### now we can build a counter or histagram code

#counts = dict()   #here we created an empty bucket to do things with
#list = ['csev', 'cwen', 'csev', 'zqian', 'cwen']  # list of names we might have drawn out of a file or somthing
#for name in list:
    #if name not in counts:
        #counts[name] = 1
    #else:
        #counts[name] = counts[name] + 1
#print(counts)


########## This is so common that there is already a built in method to make this easy for us
#it collaspes these 4 lines of code into the '.get' method 

#if name in counts:
    #x = counts[name]
#else:
    #x = 0

#x = counts.get(name,0) # this line is equal to the 4 lines above
#that allows us to condense the above loop into one line

counts = dict()
list = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in list:
    counts[name] = counts.get(name, 0) + 1 #treat this like an idiom --> allows you to make new entries in dictionaries and count them by adding one to them
print(counts)                              # zero is the starting value and basically says if somthing is new make it one -- if a 1 were there the first time you saw it would count it to 2
                                           #it is essentially creating a dictionary init of itself, zero is a defined default 
                                     
### get also works as an excellent way to invoke what you want out of a dictionary

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x) 

#x will print 'Mustang'
#########################################################


#counts = dict()
#print('Enter a line of text:')
#line = input('')

#words = line.split()

#print('Words:', words)

#print('Counting...')
#for word in words:
#    counts[word] = counts.get(word,0) +1
#print('Counts', counts)

#####
#definite loops in dictionaries

counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:       #for each of the keys
    print(key, counts[key])  #print out the tag and then the associated value

#### retrieving exactly what you want from the dictionary
#Here are a few methods that allow you to retrieve keys, values, or both from a dictionary

x = 'blue'
jjj = {'clown' : 100, 'cowboy': 'yeehaw', 'apple' : x }

print(jjj.keys())  #prints off a list of the keys

print(jjj.values()) #prints off a list of values

print(jjj.items())  #prints off both


### looping through key value pairs in a dictionary using two iteration variables
# in the iteration pair the first value is the key and the second is the corisponding value

xxx = {'clown' : 100, 'cowboy': 'yeehaw', 'apple' : x }
for aaa,bbb in xxx.items():
    print (aaa, bbb)





########### looping through files