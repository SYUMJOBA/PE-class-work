import menuFunctions


#Welcoming of the user in the program
print("Welcome to the controllable immune system scheme drawer!")
print("Type 'help' for a quick list of commands", end = "\n\n")
scale = int(input("Please enter a certain scale, the default is 1: "))

#Initializing the program for real
#Here the program just keeps asking the user a something to input, and that, if it will match with something of the defined functions, it will do the action connected

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
    elif x == "Cell Types":
        menuFunctions.ListCellTypes()
    elif x == "Cell Listing":
        menuFunctions.ListCellsWithFunctions()
    elif x == "F" or x == "f": # here begins the turtle direct functions
        menuFunctions.TurtleForward()
    elif x == "sh" or x == "SH":
        menuFunctions.turtleSetheading()
    elif x == "C" or x == "c":
        menuFunctions.turtleSetColor()
    elif x == "Start fill" or x == "start fill":
        menuFunctions.turtleStartFill()
    elif x == "End fill" or x == "end fill":
        menuFunctions.turtleEndFill()
    elif x == "Goto" or x == "goto":
        menuFunctions.TurtleGoto()
    elif x == "Cir" or x == "cir":
        menuFunctions.TurtleDoCircle()
    elif x == "Up" or x == "up":
        menuFunctions.TurtlePullUp()
    elif x == "Down" or x  == "down":
        menuFunctions.turtlePullDown()
    elif x == "Left" or x == "left":
        menuFunctions.turtleTurnLeft()
    elif x == "Rigth" or x == "right":
        menuFunctions.turtleTurnRight()
    elif x == "Misc" or "misc":
        menuFunctions.DoRandomTurtleMisc()
    else:
        print("Command typed appeared to be inexistent or unknown")
        print()
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
print("_FOR CONTRIBUTION___________________________________________________")
print("|Project hosted on github: https://github.com/SYUMJOBA/PE-class-work")
print("|___________________________________________________________________")
print()
input("Press ENTER to exit the program")