score = input("Enter Score between 0.0 and 1.0: ")
gs = float(score) #gradeable Score

if gs > 1.0:
    print('invalid entry. please try again')

elif gs > 0:
    if gs >= 0.9:
        print('A')
    elif gs >= 0.8:
        print('B')
    elif gs >= 0.7:
        print('C')
    elif gs >= 0.6:
        print('D')
    elif gs < 0.6:
        print('F')

else:
    print('invalid entry. please try again')
