import turtle
import Functions_colors
t = turtle.Turtle()


def drawMacrophage(posX=0, posY=0, scale=1):

    #initialize the pen and bring it in position
    t.penup()
    t.goto(posX, posY)
    t.setheading(0)
    t.pendown()

    #draw the first sector
    t.color(Functions_colors.colours["Cause inflammation"]) #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
    t.begin_fill()
    t.forward(60*scale)
    t.left(90)
    t.circle(60*scale, 120)
    t.left(90)
    t.forward(60)
    t.end_fill()

    #draw the second sector
    t.setheading(120)
    t.color(Functions_colors.colours["Activate other cells"]) #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
    t.begin_fill()
    t.forward(60*scale)
    t.left(90)
    t.circle(60*scale, 120)
    t.left(90)
    t.forward(60)
    t.end_fill()

    #draw the third sector
    t.setheading(0)
    t.color(Functions_colors.colours["Communicate"]) #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
    t.begin_fill()
    t.setheading(-120)
    t.forward(60)
    t.left(90)
    t.circle(60, 120)
    t.left(90)
    t.forward(60)
    t.end_fill()

    #draw the central circle
    t.penup()
    t.goto(posX, posY)
    t.forward(40*scale)
    t.left(90)
    t.color(Functions_colors.colours["Kill enemies"]) #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
    t.pendown()
    t.begin_fill()
    t.circle(40*scale)
    t.end_fill()

    #done

#I'll try making a better function here
#here the code works pretty in a complex shape ... basically the turtle loops trough the cell's characteristics to design it, sector by sector.
#then it will make the central cell role and that's it!
def drawCell(type, pos = [0, 0], scale = 1, rotation = "None"):

    #pos[0] is considered X
    #pos[1] is considered Y

    #memorizing the local functions of the cell type
    LocalCellFunctions = Functions_colors.cellsFunction[type]

    #checks if there are colors to be printed, if there are not, it will terminate the function
    if len(LocalCellFunctions) == 0:
        print("The selceted cell: '" + type + "' does not have any functions yet associated")
        return 0
    
    #the wideness of each circular sectors, calculated only if it can be
    Cell_radius = Functions_colors.cellsSizes[type]

    #Basically here I tell the code that ONLY if a new position is defined it has to go to new certain positions, else it will automatically draw from where it was
    #pos[0] is considered X
    #pos[1] is considered Y

    if pos != [0, 0]:
        t.penup()
        t.goto(pos[0], pos[1])
        t.pendown()
    
    if rotation != "None":
        t.setheading(rotation)

    if len(LocalCellFunctions) > 1:
        radial_angle = 360 / (len(LocalCellFunctions)-1)
        for x in range(1, len(LocalCellFunctions)):
            #this chunk of code constructs a circular sector
            t.color(Functions_colors.colours[LocalCellFunctions[x]]) #here it changes color depending on the function progressively, notice that x is used to loop trough everything
            t.begin_fill()
            t.forward(Cell_radius*scale)
            t.left(90)
            t.circle(Cell_radius*scale, radial_angle)
            t.left(90)
            t.forward(Cell_radius*scale)
            t.end_fill()
            t.left(180)

    CentralCircleWidth = 0.65    #in order for the central circle to be printed smaller inside the entire cellular area this value exists so:
                                #in order to calculate the raius of the circle, we multipy the entire radius by this constant, nontheless, this value is less than zero because is reduces it.

    #now the central circle is drawn
    t.penup()
    t.forward(Cell_radius*CentralCircleWidth*scale)
    t.color(Functions_colors.colours[LocalCellFunctions[0]])
    t.pendown()
    t.left(90)
    t.begin_fill()
    t.circle(Cell_radius*CentralCircleWidth*scale)
    t.end_fill()
    return 0

def finish():
    turtle.done()

def move(posX, posY):
    t.penup()
    t.goto(posX, posY)
    t.pendown()

def setSpeed(speed):
    t.speed(speed)

def SetBGColor(color):
    turtle.bgcolor(color)