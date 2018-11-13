import math
import turtle
x1,y1=0,0
x2,y2=100,0
x3,y3=100,100
x4,y4=0,100
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)
turtle.goto(x1,y1)
distance=math.sqrt((x3-x1)**2+(y3-y1)**2)
turtle.write(distance)
