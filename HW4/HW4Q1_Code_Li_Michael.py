#This program draws the points from unequal.txt and allows you to place a label
#anywhere on the window
from graphics import *

#read in the file and plot the points
infile = file('./unequal.txt', 'r')
win = GraphWin('Scatter Plot', 800, 700)
win.setCoords(-100,-300,700,400)
win.setBackground('black')
for line in infile:
    twoNum = line.split()
    p = Point(float(twoNum[1])*50, float(twoNum[2])*50)
    if float(twoNum[0]) == 1:
        p.setFill('red')
    elif float(twoNum[0]) == 2:
        p.setFill('yellow')
    elif float(twoNum[0]) == 3:
        p.setFill('green')
    p.draw(win)
#initial label
label = Text(Point(350,380), 'Click a place to put your label')
label.setTextColor('white')
label.draw(win)
#allow user to place the label at any location
point = win.getMouse()
label.undraw()
label = Text(point, 'Produced by Michael Li')
label.setTextColor('white')
label.draw(win)

win.getMouse()
win.close()
