import turtle
t = turtle.Turtle()


def drawMacrophage(type, posX=0, posY=0, scale=1):

    #initialize the pen and bring it in position
    t.penup()
    t.goto(posX, posY)
    t.setheading(0)
    t.pendown()

    #draw the first sector
    t.color("Cause Inflammation") #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
    t.begin_fill()
    t.forward(60*scale)
    t.left(90)
    t.circle(60*scale, 120)
    t.left(90)
    t.forward(60)
    t.end_fill()

    #draw the second sector
    t.setheading(120)
    t.color("Activate Cells") #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
    t.begin_fill()
    t.forward(60*scale)
    t.left(90)
    t.circle(60*scale, 120)
    t.left(90)
    t.forward(60)
    t.end_fill()

    #draw the third sector
    t.setheading(0)
    t.color("Communicate") #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
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
    t.color("Kill enemies") #the way that the color is called is not yet definitive, the library with the included colours is yet to be made
    t.pendown()
    t.begin_fill()
    t.circle(40*scale)
    t.end_fill()

    #done
