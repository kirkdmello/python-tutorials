import turtle
#x controls starting size of square side.
#a controls the angle of rotation.
#j controls the number of sides.
#s controls spacing between lines.


franklin = turtle.Turtle()


def spiral_shape(x,a,j,s):
    for i in range(j):
        franklin.left(a)
        franklin.forward(x+i*s)

#create spiral shape.
spiral_shape(4,30,500,1)




