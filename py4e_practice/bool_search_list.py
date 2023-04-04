found = False #False and True are their own types of variables; Boolean variables. They will return either True or False
inp = input(">")
num_inp = int(inp)
for value in [3, 12, 71, 19, 8, 32]:
    if num_inp == value:
        found = True
print(found)