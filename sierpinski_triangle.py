import turtle
from IllusionHelper import drawTriangle

turtle.speed(0) 
turtle.hideturtle()
turtle.tracer(1000, 0) # draws the design in a split second
hasDrawn = False # tells the program if the shapes have been drawn

def sierpinski(x, y, size, degree): # defines how to draw the sirepinski triangle
 drawTriangle(turtle, x, y, size, fill=False)
 if degree > 0:
    sierpinski(x, y, size/2, degree-1)
    sierpinski(x + size/2, y, size/2, degree-1)
    sierpinski(x + size/4, y + size*0.44, size/2, degree-1) 

def draw():
    global hasDrawn # this is a global variable so it can be accessed later

    if not hasDrawn:

        sierpinski(0, 0, 200, 4)

        hasDrawn = True  # changes the global variable, indicates all the shapes have been drawn
        
    else:
        turtle.penup()
        turtle.goto(0, 0) # places the pen in the center

while True:
    
    try:
        draw()  # this keeps the application "drawing" until the user exits the program otherwise it will end immediately
    except turtle.Terminator: # catches the exception if the user clicks the X button on the application
        print("Goodbye") # ends the program
        break
   
