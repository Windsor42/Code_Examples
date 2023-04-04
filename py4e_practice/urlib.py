#does the same thing as the sockets. It is just boiled down to a library to save effort
#we have to import some libraries to make it work

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
print(fhand)  #fhand is a local memory area where the data from the url now is local on your computer
for line in fhand:      #and we can do whatever we want with it now
    print(line.decode().strip())


#the urlopen eats the headers so you dont get any of that useful data we got with the socket. However, there is a way to retreive those
#you can not forget to .decode becuase b default it comes as bytes (I think VSC translates this by default however)
#here we make a histogram for the string on the page

fhand = urllib.request.urlopen('https://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)


#you can also use this to read webpages
fhand = urllib.request.urlopen('https://www.cc4e.com/') 
for line in fhand:      
    print(line.decode().strip())       #we have now accessed a link within a webpage that we could continue to follow in this terminal

#using a library to make HTML parsing a lot easier
#HTML is a bit yucky by itself so we need some tools to break it down

#SEE POSTMAN FOR VERY SIMPLE API TOOL