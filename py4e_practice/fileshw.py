#2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

#X-DSPAM-Confidence:    0.8475

#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# mbox-short.txt


count = 0
dummy = 'honk'
floatttotal= 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    
    else:
        count = count +1
        line = line + dummy
        print(line)
        atpos1 = line.find(':')
        atpos2 = line.find('honk')

        whatiwant = line[atpos1+1 : atpos2]
        print(whatiwant)
        txtvalue= float(whatiwant)
        floatttotal = floatttotal + txtvalue
        
avg = floatttotal/count
print (avg)
print("Done")