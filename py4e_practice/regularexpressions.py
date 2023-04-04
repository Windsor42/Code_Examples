#a fun and interesting topic but not a foundational one
# funtions with smart searching and smart experessions
# to use regular experessions you have to import the library using "import re"

# the following blocks of code accomplish the same task

#this block of code takes the needle in the haystack approach
#it runs through everyline of code and when it doesnt see 'From:' it returns a -1 
#it prints everthing that isnt a neg 1

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    #if line.find('From:') >= 0:
        #print(line )

#here we are using regular experessions to do the same thing
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line): #this is saying if I take the search function from the regular expression library and it finds 'From:' in the line
        print(line)              #that line will be printed

        #throwing the little carrot in there tells the regular expression to fine tune its search
        #specifically only to pull things with from if its at the begining of a line

# you can combine many regular expressions

#Python Regular Expression Quick Guide
#  ^        Matches the beginning of a line
#  $        Matches the end of the line
#  .        Matches any character
#  \s       Matches whitespace
#  \S       Matches any non-whitespace character
#  *        Repeats a character zero or more times                 #greedy will always take the largest of two options
#  *?       Repeats a character zero or more times                 #non-greedy takes the shortest or first available
#           (non-greedy)
#  +        Repeats a character one or more times
#  +?       Repeats a character one or more times 
#           (non-greedy)
#  [aeiou]  Matches a single character in the listed set          #a bracket consitutes a single character - what is in the bracket are the allowed characters to be searched
#  [^XYZ]   Matches a single character not in the listed set
#  [a-z0-9] The set of characters can include a range
#  (        Indicates where string extraction is to start
#  )        Indicates where string extraction is to end

