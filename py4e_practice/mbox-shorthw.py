fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    x = line.startswith('From')
    print(x)
    if True:
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
