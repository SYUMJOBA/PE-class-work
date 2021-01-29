#this is the definitve program that should include all libs
import random
import TurtleCells
TurtleCells.SetBGColor("black")
TurtleCells.setSpeed(0)

TurtleCells.drawCell("Natural killer cell")
TurtleCells.drawCell("Macrophage", pos= [200, 100])
TurtleCells.drawCell("Follicular dendritic cell", pos=[200, 200])
TurtleCells.drawCell("Neutrofile", pos = [-100, 0])
TurtleCells.drawCell("Mast cell")
TurtleCells.drawCell("Macrophage", pos= [-70, -100])
TurtleCells.drawCell("B cell", pos = [-300, -200])
TurtleCells.drawCell("Memory B cell", pos= [-300, -20])

for x in range(0, 60):
    a = random.choice([n for n in range(-500, 500)])
    b = random.choice([n for n in range(-400, 400)])
    TurtleCells.drawCell("Antibodies", pos= [ a , b ])



TurtleCells.move(400, 400)
TurtleCells.finish()

input("press ENTER to exit")
