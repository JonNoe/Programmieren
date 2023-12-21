import turtle

# Initialize the turtle
t = turtle.Turtle()

teich= turtle.Screen()
teich.bgcolor("white")
teich.title("Pokemon")
Schiggi = turtle.Turtle()

Schiggi.speed(0)

for j in range(360):
    Schiggi.tilt(100*j)
    Schiggi.forward(5*j)
    for i in range (20):
        Schiggi.circle(2*i)
        Schiggi.circle(-2*i)
		
		

turtle.done()