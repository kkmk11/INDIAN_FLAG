#Install turtle module in your IDLE and then execute the below program
#How to install..? 
#Go to command prompt-->Enter "pip install turtle"-->Wait untill the module installed successfully-->Exit from the command prompt-->Now run the code.
import turtle
res=turtle.Turtle()
wn=turtle.Screen()
res.hideturtle()
res.up()
res.goto(0,-200)
res.down()
res.setheading(90)
res.pensize(13)
res.forward(400)
res.pensize(3)
res.begin_fill()
res.fillcolor("red")
res.setheading(0)
res.circle(10)
res.end_fill()
res.right(90)
res.pensize(2)
res.setheading(0)
res.begin_fill()
res.fillcolor("orange")
res.forward(200)
res.right(90)
res.forward(40)
res.right(90)
res.forward(200)
res.end_fill()
res.setheading(0)
res.forward(100)
res.color("blue")
res.circle(-20)
res.right(90)
res.forward(20)
for i in range(24):
    res.left(15)
    res.forward(20)
    res.backward(20)
res.forward(20)
res.color("black")
res.begin_fill()
res.fillcolor("green")
res.left(90)
res.forward(100)
res.right(90)
res.forward(40)
res.right(90)
res.forward(200)
res.right(90)
res.forward(40)
res.right(90)
res.forward(200)
res.end_fill()
res.left(90)
res.forward(80)
res.left(90)
res.forward(200)
res.left(90)
res.pensize(13)
res.forward(400)
turtle.done()
