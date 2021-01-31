import menuFunctions


#Welcoming of the user in the program
print("Welcome to the controllable immune system scheme drawer!")
print("Type 'help' for a quick list of commands", end = "\n\n")
scale = int(input("Please enter a certain scale, the default is 1: "))

#Initializing the program for real
while True:
    x = input("Awaiting input: ")

    if x == "help" or x == "Help":
        menuFunctions.PrintHelpingMenu()
        print()
    elif x == "SetBGColor":
        menuFunctions.SetBGColor()
    elif x == "Exit" or x == "exit":
        print("Exiting the program")
        break
    elif x == "SetSpeed":
        menuFunctions.setSpeed()
    elif x == "Undo" or x  == "undo":
        menuFunctions.TurtleUndo()
    elif x == "MakeCell":
        menuFunctions.MakeCell(scale)
    else:
        print("Command typed appeared to be inexistent or unknown")
        print()


#Ending and goodbying from the program
print()
print("-- Thank you for using my sofware --")
print("$Coded by John Baxter")
print("_CONTACTS_________________")
print("|Email: syumjoba@gmail.com")
print("|Instagram: @syumjoba")
print("|_________________________")
print()
print("FOR CONTRIBUTION____________________________________________________")
print("|Project hosted on github: https://github.com/SYUMJOBA/PE-class-work")
print("____________________________________________________________________")
print()
input("Press ENTER to exit the program")