from turtle import *

speed(100)

width(7)

color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end or square

#drawing a door

forward(70)
color("blue")
begin_fill()
left(90)

forward(110)
right(90)

forward(60)
right(90)

forward(110)   #hight of the door
left(90)
end_fill()

#end to drawing door

penup()
goto(200,200)
pendown()

#drawing a roof

color("red")
begin_fill()
left(140)
forward(130)
left(80)
forward(130)
end_fill()

#end drawing roof

penup()
goto(30,125) # first window
pendown()

#drawing windows

color("green")
begin_fill()
right(130)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()


penup()
goto(125,125)  #second window
pendown()

color("green")
begin_fill()
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()

exitonclick()