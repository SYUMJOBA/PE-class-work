#this is the definitve program that should include all libs
import TurtleCells

TurtleCells.setSpeed("fastest")

TurtleCells.drawCell("Macrophage")
TurtleCells.drawCell("Macrophage", pos= [100, 200], rotation= 0)
TurtleCells.drawCell("Macrophage", pos= [-150, 200], rotation= 0)
TurtleCells.drawCell("Macrophage", pos= [100, -100], rotation= 0)

TurtleCells.move(400, 400)
TurtleCells.finish()

input("press ENTER to exit")
