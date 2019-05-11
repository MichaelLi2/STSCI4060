#This program draws the growth of a 10-year investment with user inputted
#principal and APR
from graphics import *
import random

def main():
    print 'Plotting the growth of a 10-year investment.'

    #get principal and interest rate
    principal = input('Enter initial principal: ')
    apr = input('Enter annualized interest rate: ')

    #create a graphic window
    win = GraphWin('Investment Growth Chart', 330, 260)
    win.setCoords(0,0,330,260)
    win.setBackground('white')
    ylbl = Text(Point(145,5), 'Year')
    ylbl.setSize(10)
    ylbl.draw(win)
    #create the y-axis labels
    xscale = (principal*(1+apr)**10)/4000
    for i in range(5):
        lbl = Text(Point(21,230-i*50), str(round(xscale,1)*(4-i))+'K')
        lbl.setSize(8)
        lbl.draw(win)
    #create the x-axis labels
    for j in range(11):
        lbl = Text(Point(40+j*24,20), str(j))
        lbl.setSize(8)
        lbl.draw(win)
    #draws the bars
    barHeight = 200*principal/(principal*(1+apr)**10)
    for k in range(11):
        bar = Rectangle(Point(k*25+40, 30), Point(k*25+65, 30+barHeight))
        bar.setFill(color_rgb(random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        bar.draw(win)
        barHeight = barHeight*(1+apr)

    raw_input('Press <Enter> to quit')
    win.close()

main()
