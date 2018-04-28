import turtle
#circle of squares project

franklin = turtle.Turtle()
#length of square
x = 50
#repetitions
j = 500
#brush size
bs = 1

def square(x):
    for n in range(4):
        franklin.forward(x)
        franklin.right(90)



franklin.pensize(bs)
franklin.speed(1000)
for i in range(j):
    franklin.right(90)
    franklin.right(7)
    square(x)


    



