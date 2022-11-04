import turtle

print(turtle.pos())  # debugging position
turtle.hideturtle()

x = 0


def my_circle(circle_size=x):
    turtle.color("blue")
    turtle.pensize(3)
    turtle.circle(circle_size)


y = 0


def my_triangle(triangle_size=y):
    turtle.color("red")
    turtle.pensize(6)
    turtle.forward(triangle_size)
    turtle.left(120)
    turtle.forward(triangle_size)
    turtle.left(120)
    turtle.forward(triangle_size)


z = 0


def my_square(square_size=z):
    turtle.color("green")
    turtle.pensize(3)
    turtle.backward(square_size)
    turtle.right(90)
    turtle.forward(square_size)
    turtle.left(90)
    turtle.forward(square_size)
    turtle.left(90)
    turtle.forward(square_size)


# -------draw ears------------
x = 15
my_circle(x)
x = 25
my_circle(x)
# move to the next ear
turtle.penup()
turtle.forward(120)
turtle.pendown()
x = 15
my_circle(x)
x = 25
my_circle(x)

# -------draw face-------------
z = 120
my_square(z)
print("face -")
print(turtle.pos())  # debugging position
# ------------ draw the eyes
x = 5
# position the cursor
turtle.penup()
turtle.right(45)
turtle.backward(45)
turtle.pendown()

my_circle(x)  # eye 1
turtle.penup()
turtle.right(45)
turtle.backward(45)
turtle.pendown()
my_circle(x)  # eye 2

# ------------draw the lips--------

turtle.penup()
print("lips-")
print(turtle.pos())  # debugging starting position
turtle.right(90)
turtle.forward(35)
turtle.pendown()
turtle.color('red')
x = 25
turtle.circle(x, 180)


# -------draw the nose-------------
turtle.penup()
# position the cursor
print("nose-")
print(turtle.pos())  # debugging position
turtle.left(45)
turtle.forward(15)
turtle.pendown()
y = 25
my_triangle(y)

# ---finish --------------
turtle.hideturtle()
input("Did you like me?")
print("thank you")
