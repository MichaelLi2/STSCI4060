#This program is a user interactive temperature converter from Celsius to Fahrenheit
from graphics import *

def main():
    win = GraphWin("Temperature Converter", 300, 200)
    win.setCoords(0,0,300,200)

    #Draw the interface
    Text(Point(90,150), "Celsius Temperature:").draw(win)
    Text(Point(95,100), "Farenheit Temperature:").draw(win)
    inpC = Entry(Point(180,150), 5)
    inpC.draw(win)
    inpF = Entry(Point(190,100), 5)
    inpF.draw(win)
    #button
    rect = Rectangle(Point(100,20), Point(200,70))
    rect.setFill('yellow')
    rect.draw(win)
    rect.setOutline('red')
    button = Text(Point(150,45), 'Convert It')
    button.draw(win)

    #wait for mouse click to convert and then quit
    quit = False
    converted = False
    while not quit:
        coord = win.getMouse()
        #if mouse click is within button
        if coord.getX() > 100 and coord.getX() < 200 and coord.getY() > 20 and coord.getY() < 70:
            #Check if at least one of the entries is filled
            if inpF.getText() != '' or inpC.getText() != '':
                if converted:
                    quit = True
                elif inpF.getText() != '' and inpC.getText() != '':
                    print "Both entries filled, don't know which to convert"
                else:
                    #convert input
                    if inpF.getText() != '':
                        farenheit = eval(inpF.getText())
                        inpC.setText(str(5.0/9.0 * (farenheit - 32)))
                    else:
                        celsius = eval(inpC.getText())
                        inpF.setText(str(9.0/5.0 * celsius + 32))
                    converted = True
                    button.setText('Quit')

    win.close()

main()
