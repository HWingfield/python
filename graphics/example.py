from graphics import *

# Create a window of a suitable size
window = GraphWin("Visualisation", 300, 300)

# Create and draw a circle
ball = Circle(Point(100,100), 30)
ball.setFill(color_rgb(255,255,0))
ball.draw(window)

# Create and draw a rectangle
box = Rectangle(Point(200,50),Point(250,150))
box.setOutline(color_rgb(255,0,0))
box.draw(window)

# Create and draw a line
line = Line(Point(200,200),Point(250,280))
line.setWidth(4)
line.draw(window)

# Create and draw some text
text = Text(Point(50,200),"Hello")
text.draw(window)

# Wait until the mouse is clicked before closing the window
window.getMouse()
