#this library is a set of functions witch shortens a lot the turtle graphics and eases the development, instead of defining and using functions in controllabl scheme, functions will be called from here

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
    print(" Type: 'C' to chanhe your pen's color")
    print(" Type: 'Start Fill' to start filling a shape, this works strictly related with t.begin_fil()")
    print(" Type: 'End Fill' to end filling a shape, this works strictly related with t.begin_fil()")
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

def ListCellsWithFunctions():
    print("_Cell_Listing_with_functions____________________________________________________________________________________________________________________________________|")
    print("________________________________________________________________________________________________________________________________________________________________|")
    count = 0
    for key in TurtleCells.Functions_colors.cellsFunction:
        count += 1
        print(str(count) + tab(len(str(count)) , 5) + "|" + key + tab(len(key), 30), end = "|")
        for function in TurtleCells.Functions_colors.cellsFunction[key]:
            print(function + tab(len(function), 30), end = "|")
        print()
        print(tab(ShouldSpace = 5) + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|" + tab(0, 30, "-") + "|")

    print("     |__________________________________________________________________________________________________________________________________________________________|")
    print()