#where it all pays off!!

#open() function
#returns a "file handle" - a variable used to perform operations on the file
#works like 'file --> open' in a word processor

fhand = open('nuclearlaunchcodes.txt')
print(fhand)

#newline '\n' makes a new line
# it also counts as a single character 

stuff = 'Howdy\nWorld!'
print (stuff)
print (len(stuff))

xfile = open('nuclearlaunchcodes.txt')
for lines in xfile:                    #lines is an iterative variable, it could be named anything
    print(lines)                       #the file has been opened and lines runs through each line grabs it and prints it out

#this leaves you with a lot of whitespace 
#you can use the .rstrip() function to get rid of this white space like in the following code

print ('  ')

fhand = open('nuclearlaunchcodes.txt')
for line in fhand:
    line = line.rstrip()
    print(line)

#you can make a custom point to quit the program by putting in a quit() this stops the file from executing

fname = input('Please enter file name:    ')
try:
    fhand = open(fname)
except:
    print('File could not be found', fname)
    quit()

count = 0
for line in fhand:
    line = line.lower()
    print(line)
    if "secret" in line:
        count = count + 1
        continue
print('there are', count, 'lines with secrets in this document')
    

