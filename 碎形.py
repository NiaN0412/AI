import turtle

window = turtle.Screen()
window.delay(10)

t = turtle.Turtle()

t.shape("turtle")
t.pensize(2)
t.color("green")

# Begin of your code
t.penup()
t.goto(0,200)
t.right(60)
t.pendown()
t.forward(270)
t.right(120)
t.forward(270)
t.right(120)
t.forward(270)
# End of your code

window.exitonclick()
