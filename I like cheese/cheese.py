import os
dead = True
while dead:
    cost = 0.00
    #this is the welcome message and the asking if you want a sadwhich
    print("Hello welcome to Jersey Mikes were you get what you derserved")
    sandwhich = input("would you like to get a sandwich. (y/n): ")
    if sandwhich == "n":
        print("well too bad that is all we got.")
    #this is them asking for what size you want on you sandwhich
    size = input("ok what size of sandwich would you like, large(4.50), medium(3.50), or small(2.50) *shows sand*: ")
    if size == "large":
        cost += 4.50
    elif size == "medium":
        cost += 3.50
    elif size == "small":
        cost += 2.50
    else:
        input("You Died, press enter to continue")
        os.system("cls")
        break
    #this asks for what side you want
    side = input("ok now want side do you want, fries(1.50), chips(1.00), apples(1.25), or crisps(1.25): ")
    if side == "fries":
        cost += 1.50
    elif side == "chips":
            cost += 1.00
    elif side == "apples":
            input("You Died, press enter to continue")
            os.system("cls")
            break      
    elif side == "crisps":
            input("You Died, press enter to continue")
            os.system("cls")
            break
        #this asks for what kinda a drink you want
    drink = input("ok now for a drink would you like Root Beer(2.00), Sprite(1.25), Dr.Pepper(1.50), or our new spiciest drink Nuka-Cola(1.75): ")
    if drink == "Root Beer" or drink == "Root beer" or drink == "root beer" or drink == "rootbeer":
        cost += 2.00
    elif drink == "Sprite" or drink == "sprite":
        cost += 1.25
    elif drink == "Dr.Pepper" or drink == "dr.pepper" or drink == "dr pepper" or drink == "Dr Pepper" or drink == "Dr pepper":
        cost += 1.50
    elif drink == "Nuka-Cola" or drink == "Nuka Cola" or drink == "nuka cola" or drink == "nukacola":
        input("You Died, press enter to continue")
        os.system("cls")
        break
    #this asks for what kinda meat you want
    meat = input("Oh I am sorry I forgot to ask for what kinda meat you want on the sandwich, beef(1.00), pork(1.50), or turkey(99.99): ")
    if meat == "turkey":
        cost += 99.99
    else:
        turkey = input("oh sorry we are out of that, we only have turkey would you like it, (y/n): ")
        if turkey == "n":
            input("You Died, press enter to continue")
            os.system("cls")
            break
        elif turkey == "y":
            cost += 99.99
    #and this is the reuse button that i don't think actually serves much of a purpose
    reuse = input("ok and you total is $" + str(cost) + " would you like to order anything else. (y/n): ")
    if reuse == "n":
        input("You Died, press enter to continue")
        os.system("cls")
    
    os.system("cls")
    