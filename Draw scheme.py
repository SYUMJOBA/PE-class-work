#this is the definitve program that should include all libs
import random
import TurtleCells
TurtleCells.SetBGColor("black")


TurtleCells.drawCell("Natural killer cell")
TurtleCells.drawCell("Macrophage", pos= [200, 100])
TurtleCells.drawCell("Follicular dendritic cell", pos=[200, 200])
TurtleCells.drawCell("Neutrofile", pos = [-100, 0])
TurtleCells.drawCell("Mast cell")
TurtleCells.drawCell("Macrophage", pos= [-70, -100])
for x in range(0, 30):
    a = random.choice([n for n in range(-400, 400)])
    b = random.choice([n for n in range(-300, 300)])
    TurtleCells.drawCell("Antibodies", pos= [ a , b ])


TurtleCells.move(400, 400)
TurtleCells.finish()

input("press ENTER to exit")
