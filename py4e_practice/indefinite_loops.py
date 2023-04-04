while True: #this means the while questions is always true and will continue to run until a break
    line = input('>')
    if line[0] == '#': #line[0] seems to read the first character in the string
        continue #if the first character in the string is # the continue function procs and starts the loop over
    if line == 'done': #if the string is == 'done' we proc the break and exit the loop
        break
    print(line) #otherise the loop is continued in this function 
print('Done!')