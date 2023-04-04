#this is how we get into a file and make an output for the most used word and how often it is used

##Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

counts = dict()
names = list()

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)


for line in fh:
    line.rstrip()
    if not line.startswith('From:'): continue
    pos1 = line.find(': ')
    pos2 = line.find('@')
    name = (line[pos1+2:pos2])
    names.append(name)


for people in names:
    counts[people] = counts.get(people, 0)+1

print(counts)

bigcount = None
bigword = None

for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print ('I see the word "',bigword,'"', bigcount, 'times') 