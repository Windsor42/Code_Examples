fname = input("Enter file name: ")
fh = open(fname)
lst = list()
res = list()
for line in fh:
    strpline = line.rstrip()
    #print(strpline)
    splitline = line.split()
    #print(splitline)
    for word in splitline:
        lst.append(word)

lst.sort()
#print(lst)

for srtword in lst:
    if srtword not in res:
        res.append(srtword)
print(res) 