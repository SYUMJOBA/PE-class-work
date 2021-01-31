#this library is a set of functions witch shortens a lot the turtle graphics and eases the development, instead of defining and using functions in controllabl scheme, functions will be called from here

import TurtleCells

def PrintHelpingMenu():
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
