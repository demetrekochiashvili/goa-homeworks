from turtle import *

#we want to paint a house

speed(10)
#step 1: draw a square
width(7)
begin_fill
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill
forward(200)
left(90)
#end of square

#drawing a door
begin_fill()

forward(70)
color("yellow") 
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()
 
 #end of door

#drawing roof

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)

end_fill()


#end of roof


#drawing a window
forward(5)
right(90)



penup()
goto(185,140)
pendown()
begin_fill()
left(30)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()
#second window
penup()
goto(65,140)
pendown()
begin_fill()
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
end_fill()





exitonclick()
