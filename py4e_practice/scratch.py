import urllib.request, urllib.parse, urllib.error

fhand = 'I am a little fat girl with pig tails and a skirt'
print(fhand)  #fhand is a local memory area where the data from the url now is local on your computer
for line in fhand:      #and we can do whatever we want with it now
    print(line.strip())


#the urlopen eats the headers so you dont get any of that useful data we got with the socket. However, there is a way to retreive those
#you can not forget to .decode becuase b default it comes as bytes (I think VSC translates this by default however)
#here we make a histogram for the string on the page

counts = dict()
for line in fhand:
    words = line.split()
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)