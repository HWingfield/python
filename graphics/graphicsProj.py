from graphics import *

# Create a window of a suitable size
window = GraphWin("Visualisation", 400, 400)

numberlist = []


text_file = open("numbers.txt")
content_of_file = text_file.readlines()
for results in content_of_file:
    numberlist.append(int(results))
text_file.close()

ball = Circle(Point(225,250), 100)
ball.setFill(color_rgb(0,0,0))
ball.draw(window)

apass = []
#40-50
bthird = []
#50-60
cabove = []
#cabove 60

for everyNumber in numberlist:
    if (everyNumber < 50):
        line = Line(Point(200,200),Point(250,280))
        line.setWidth(8)
        line.setFill(color_rgb(255,0,0))
        line.draw(window)
        apass.append(everyNumber)
    if (everyNumber <= 60) and (everyNumber > 50):
        line = Line(Point(100,100),Point(250,280))
        line.setWidth(8)
        line.setFill(color_rgb(0,255,0))
        line.draw(window)
        bthird.append(everyNumber)
    if (everyNumber >= 60):
        line = Line(Point(50,60),Point(250,280))
        line.setWidth(8)
        line.setFill(color_rgb(0,0,255))
        line.draw(window)
        cabove.append(everyNumber)

line = Line(Point(200,200),Point(250,280))
line.setWidth(8)
line.setFill(color_rgb(255,0,0))
line.draw(window)

#line.setOutline("blue")


window.getMouse()
