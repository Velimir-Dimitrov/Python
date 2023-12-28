import turtle

colors = ['red', 'blue', 'yellow']
turtle.speed(0)
turtle.pensize(10)

for i in range(200):
    turtle.color(colors[i % 2])
    turtle.forward(i * 2)
    turtle.left(89)

turtle.done()