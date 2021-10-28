import turtle

# 画正方形
import future.backports.socketserver


def drawSqure():
    t = turtle.Turtle()
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    turtle.done()

# 画五角星
def drawStar():
    t = turtle.Turtle()
    for i in range(5):
        t.forward(100)
        t.right(144)
    t.hideturtle()
    turtle.done()

# 画回字格
def drawHui(t,length):
    if length > 0:
        t.forward(length)
        t.right(90)
        drawHui(t, length - 5)

    turtle.done()


# 画分形树
def drawTree(brance_len):
    if brance_len > 5:
        t.forward(brance_len)
        t.right(20)
        drawTree(brance_len - 15)
        t.left(40)
        drawTree(brance_len - 15)
        t.right(20)
        t.backward(brance_len)



# drawSqure()
# drawStar()
# t = turtle.Turtle()
# drawHui(t, 100)

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('green')
t.pensize(2)
drawTree(105)
t.hideturtle()
turtle.done()