# Introduction narration of game


loop = 1
print("---------------------------------------------------------")
print("Welcome to The Dungeon Of The Rat King")

print('')
print('')
print('')
print('')
print('      /+\/+\/+\    ')
print('      \  \/  /         _,-"~^"-.')
print('       \_/__/    _,-"~`         `.')
print('     ." ( /`"-,-"`                 ;')
print('    / /6                             ;')
print('   /           ,             ,-"     ;')
print('  (,__.--.      \           /        ;')
print('   //''   /`-.\   |          |        `._________')
print('     _.-''_/`  )  )--...,,,___\     \-----------,)')
print('   ((("~` _.-''.-''           __`-.   )         //')
print('        ((("`             (((---~"`         //')
print('                                            ((________________')
print('                                            `----""""~~~~^^^```')

inventory = list()


while True:
    # First Input Loop
    while loop == 1:
        if loop == 1:
            print("---------------------------------------------------------")
            print("You have been sent from your village to investigate the strange dissapearance of cattle.")
            print("Following the tracks of strange animals you've found the mouth of a cave. It is littered with the bones of cow, sheep, and somthing else you can't put your finger on")
            print("You've made camp for the night just outsdie the cave. Firelight flickers on the walls and the dancing shadows bring an eerie life to the bones strewn about.")
            first = input("What do you do? ")

        if first.lower() == ("leave"):
            print("---------------------------------------------------------")
            print("You think to yourself 'whats a few sheep and cows now and again?' and head home.")
            print("The problem worsens and worsens and come winter you find yourself across and empty bowl with an empty stomach wondering what you could have done differently")

            exit_inp = input("Do you want to continue? Y/N ")
            
            if exit_inp.lower() == ("n"):
                exit()
            elif exit_inp.lower() == ("y"):
                loop = 1
            
        elif first.lower() == ("check supplies"):
            print("---------------------------------------------------------")
            print("You take a look inside of your backpack at the meager supplies you brought with you.")
            print('Youre current inventory contains the following')
            inventory.append('Goat Jerky')
            inventory.append('Small Knife')
            inventory.append('Canteen of Water')
            inventory.append('Flint and Steel')
            inventory.append('A few gold pieces')
            print(inventory)
            loop = 2

        else:
            print("---------------------------------------------------------")


#loop where player checked their inventory
#player has access to their inventory at this point otherwise it will be empty --> loop 3
    while loop == 2:
        if loop == 2:
            print("---------------------------------------------------------")
            print("Taking note of this you gather your supplies and sling your backpack over your shoulder")
            print("You face the cave")
            second = input("What do you do? ")
        
        if second.lower() == ("leave"):
            print("---------------------------------------------------------")
            print("You think to yourself 'whats a few sheep and cows now and again?' and head home.")
            print("The problem worsens and worsens and come winter you find yourself across and empty bowl with an empty stomach wondering what you could have done differently")

            exit_inp = input("Do you want to continue? Y/N ")
            
            if exit_inp.lower() == ("n"):
                exit()
            elif exit_inp.lower() == ("y"):
                loop = 1
        
        elif second.lower() == ('sleep'):
            print('Its very uncomfortable to sleep with a backpack on your back')

# Exit loop at the end of game
    #exit_inp = input("Do you want to continue? Y/N ")
        #if exit_inp.lower() == ("n"):
        	#exit()
       # if exit_inp.lower() == ("y"):
        	#loop = 1
