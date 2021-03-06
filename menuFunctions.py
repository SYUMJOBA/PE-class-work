#this library is a set of functions witch shortens a lot the turtle graphics and eases the development, instead of defining and using functions in controllabl scheme, functions will be called from here

import MakeText
import TurtleCells

#This function gets called when tabbing is necessary
def tab(OccupiedSpace = 0, ShouldSpace = 20, charToUse = " "):
    #ShouldSpace indicates the space occupied by the word plus the space indicated by the spaces that there should be after the word
    #tabbing is the final result of spaces
    #OccupiedSpace is the space already occupied by the word
    tabbing = ""
    for n in range(0, ShouldSpace-OccupiedSpace, 1):
        tabbing = tabbing + charToUse
    return tabbing

#this is a bunch of text printed out as help, listing commands to corresponding functions. I still have to add the commands to print the text on the screen.
def PrintHelpingMenu():
    print("------COMMAND LIST-----------------------------------------------")

    print("__GENERAL_PRINCIPAL_COMMANDS: ___________")
    print(" Type: 'SetBGColor' to set a background colour")
    print(" Type: 'MakeCell' to print a cell on the screen")
    print()
    print()
    print("__Pen charateristics: _____________")
    print(" Type: 'SetSpeed' to set a different speed for the pen")
    print(" Type: 'Undo' to undo an action")
    print()
    print("__Helpings: _______________________")
    print(" Type: 'Cell Types' if you want a listing of all registered cell types")
    print(" Type_ 'Cell Listing' if you want to see al different cells with theyr own functions listed")
    print()
    print("__Pen Controls: ___________________")
    print(" Type: 'F' to make the pen go forward")
    print(" Type: 'SH' to set your pen's heading at some degree ")
    print(" Type: 'C' to change your pen's color")
    print(" Type: 'Start fill' to start filling a shape, this works strictly related with t.begin_fil()")
    print(" Type: 'End fill' to end filling a shape, this works strictly related with t.begin_fil()")
    print(" Type: 'Goto' to tell the pen to go to a certain position")
    print(" Type: 'Cir' to begin creating a circle")
    print(" Type: 'Up' to stop the pen from writing")
    print(" Type: 'Down' to land the pen on the paper")
    print(" Type: 'Left' to turn the pen left")
    print(" Type: 'Right' to turn the pen right")
    print("-----------------------------------------------------------------")

def SetBGColor():
    color = input("enter the color here: ")
    TurtleCells.SetBGColor(color)

def setSpeed():
    speed = input("Enter here the speed: ")
    TurtleCells.t.speed(speed)

def TurtleUndo(Times = 1):
    for x in range(0, Times):
        TurtleCells.t.undo()

#this function prints a cell on the screen according to the selected scale (at the opening of the program) and type (selected at the moment of printing). 
#If there isn't any match with cell types it will just skip everything, print a message that explains the user that the cell type is invalid and exit the function

#this function checks if a string value is convertable into an integer number, it will be very useful to avoid user mistakes when inputting values
StringNums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
def IsStringConvenrtableToInt(word):
    for char in word:
        if char not in StringNums:
            return False
            break
        else:
            continue
    return True


def MakeCell(SelectedScale):
    Cell_Type = input("Please enter the Cell Type: ")
    if Cell_Type in TurtleCells.Functions_colors.cellsFunction:
        x = int(input("Please enter X position: "))
        y = int(input("Please enter Y position: "))
        TurtleCells.drawCell(Cell_Type, pos= [x, y], scale = SelectedScale)
    else:
        print("Please retry and enter a valid Cell type")
        print()


def ListCellTypes():
    print("------CELL LISTING--------------------------")
    print("The registered cells are all the following: ")
    for key in TurtleCells.Functions_colors.cellsFunction:
        print(" " + key)

def ListCellsWithFunctions(): #this function prints an entire listing of cells with theyr functions in a sheet
    print("_Cell_Listing_with_functions____________________________________________________________________________________________________________________________________.")#this prints the top line
    print("________________________________________________________________________________________________________________________________________________________________|")
    count = 0
    for key in TurtleCells.Functions_colors.cellsFunction: #this loop prints the entire sheet by itself
        count += 1
        print(str(count) + tab(len(str(count)) , 5) + "|" + key + tab(len(key), 30), end = "|") # this prints the name and the cell's index

        functionsPrinted = 0
        for function in TurtleCells.Functions_colors.cellsFunction[key]: # this prints the function associated to the cell
            functionsPrinted += 1
            print(function + tab(len(function), 30), end = "|")

        if functionsPrinted < 5:
            for time in range(1, 5 - functionsPrinted): # this completes the line, if the functions did not go through the full width if the sheet, so it's a "completition" function
                print(tab(0, 30), end="|")


        print() # newline

        # this prints another sheet line, giving more space to the cell's name
        print(tab(ShouldSpace = 5), end = "|")
        for x in range(0, 5):
            print(tab(ShouldSpace = 30), end = "|")

        print() # newline
        print(tab(ShouldSpace = 5) + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|")# this creates a separatory row for the sheet

        #and the process repeats every single cell founf in the dictionary

    print("     |__________________________________________________________________________________________________________________________________________________________|") # this prints the bottom line
    
    print() # final newline to detach the function's result from the rest of the program output

def TurtleForward():
    length = input("Enter how forward you want to go: ")
    if IsStringConvenrtableToInt(length):
        length = int(length)
    else:
        print("Please enter just an integer number for this")
        return 0
    TurtleCells.t.forward(length)

def turtleSetheading():
    angle = int(input("Enter the angle you want to set the pen at: "))
    TurtleCells.t.setheading(angle)

def turtleSetColor():
    color = input("Enter the color you want to set for the pen: ")
    TurtleCells.t.color(color)

def turtleStartFill():
    TurtleCells.t.begin_fill()

def turtleEndFill():
    TurtleCells.t.end_fill()

def TurtleGoto():
    x = int(input("Enter the X position: "))
    y = int(input("Enter the Y position: "))
    TurtleCells.t.goto(x, y)

def TurtleDoCircle():
    radius = int(input("Enter circle radius: "))
    extent = input("Enter circular angle width: ")
    if extent == "":
        extent = 360
    else:
        extent = int(extent)
    TurtleCells.t.circle(radius, extent)

def TurtlePullUp():
    TurtleCells.t.penup()

def turtlePullDown():
    TurtleCells.t.pendown()

def turtleTurnLeft():
    angle = int(input("Enter the rotation angle value: "))
    TurtleCells.t.left(angle)

def turtleTurnRight():
    angle = int(input("Enter the rotation angle value:"))
    TurtleCells.t.right(angle)


    #this is an additional set of instructions for other misc functions that can be activated from the user
def DoRandomTurtleMisc():
    inputVar = input("Awaiting input for Misc: ")
    
    if inputVar == "help" or inputVar == "Help":
        print()
        print( "_MISC_HELP____________________________________________________________  " )
        print( "| Type 'Flood antibodies' to flood the screen with small antibodies     " )
        print( "| Type 'help' to show the help tab (well you are watching it now ...)   " )
        print( "______________________________________________________________________  " )
    elif inputVar == "Flood antibodies" or inputVar == "flood antibodies":
        TurtleCells.FloodAntibodies()
    else:
        print("The typed word did not correspond to any command, returning to basic")