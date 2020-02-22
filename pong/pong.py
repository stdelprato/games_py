
import turtle

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width = 800, height = 600)
wn.tracer(0)


# palito de la izquierda

paloA = turtle.Turtle()
paloA.speed(0)
paloA.shape('square')
paloA.color('white')
paloA.penup()
paloA.goto(-350, 0)


# palito de la derecha


# pelotonga



# main game loop

while True:
    wn.update()
