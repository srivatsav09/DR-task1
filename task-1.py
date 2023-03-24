import turtle
wn = turtle.Screen()
wn.bgcolor("white")
skk = turtle.Turtle()
skk.fillcolor("pink")


skk.begin_fill()
skk.left(135)

#center petal
for i in range(90):
    skk.forward(2)
    skk.right(1)
skk.right(90)
for i in range(90):
    skk.forward(2)
    skk.right(1)
skk.forward(1)
skk.right(72)

#first petal
for i in range(85):
    skk.forward(2)
    skk.right(1)
skk.right(150)

for i in range(30):
    skk.forward(2)
    skk.left(1)
skk.penup()
skk.goto(0,0)
skk.pendown()
skk.forward(1)
skk.left(80)

for i in range(85):
    skk.forward(2)
    skk.left(1)
skk.left(150)

for i in range(30):
    skk.forward(2)
    skk.right(1)
skk.penup()
skk.goto(0,0)
skk.pendown()
skk.forward(1)
skk.right(65)

#second petal
for i in range(75):
    skk.forward(2)
    skk.right(1)
skk.right(140)

for i in range(20):
    skk.forward(2)
    skk.left(1)
    
skk.penup()
skk.goto(0,0)
skk.pendown()
skk.forward(1)
skk.left(40)

for i in range(75):
    skk.forward(2)
    skk.left(1)
skk.left(140)

for i in range(22):
    skk.forward(2)
    skk.right(1)
skk.end_fill()
skk.penup()
skk.goto(0,0)
skk.pendown()
skk.forward(1)
skk.right(5)

#leaf
skk.fillcolor("green")
skk.begin_fill()
for i in range(50):
    skk.forward(2)
    skk.right(1)
for i in range(140):
    skk.forward(0.1)
    skk.right(1)
for i in range(48):
    skk.forward(2)
    skk.right(1)
skk.penup()
skk.goto(0,0)
skk.pendown()
skk.forward(1)
skk.left(13)

for i in range(50):
    skk.forward(2)
    skk.left(1)
for i in range(140):
    skk.forward(0.1)
    skk.left(1)
for i in range(48):
    skk.forward(2)
    skk.left(1)
skk.end_fill()
    

