#Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 


counts = dict()
timecount = list()

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)

for line in fh:
    line.rstrip()
    if not line.startswith('From '): continue
    pos1 = line.find('  ')
    pos2 = line.find(':')
    name = (line[pos1+4:pos2])
    timecount.append(name)


for hours in timecount:
    counts[hours] = counts.get(hours, 0)+1

for k,v in sorted(counts.items()): 
    print(k,v)