import turtle
from IllusionHelper import drawTriangle


turtle.speed(0) 
turtle.hideturtle()
turtle.tracer(1000, 0)
hasDrawn = False 

def sierpinski(x, y, size, degree):
    colours = ['blue','red','pink','white','yellow',
    'violet','orange']
    drawTriangle(turtle, x, y, size, colours[degree])
    if degree > 0:
        sierpinski(x, y, size/2, degree-1)
        sierpinski(x + size/2, y, size/2, degree-1)
        sierpinski(x + size/4, y + size*0.44, size/2, degree-1)

def draw():
    global hasDrawn
    if not hasDrawn:

        sierpinski(0, 0, 200, 4)

        hasDrawn = True
        
    else:
        turtle.penup()
        turtle.goto(0, 0)

while True:
    
    try:
        draw()
    except turtle.Terminator:
        print("Goodbye")
        break
   
