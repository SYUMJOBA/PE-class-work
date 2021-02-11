
import turtle
t = turtle.Turtle()

#This should work as a library that lets me print text on the screen

#So the central function is printLetter, it takes a letter as argument, then it loops it through a gigantic if-elif-else. I know that it's efficient as me at school (poorly) but it will do the job and as now I can't think of a better way, I'll maybe restructure the code later.


def printLetter(letter, scale = 1):
    if letter == "a" or letter == "A":
        t.begin_fill()