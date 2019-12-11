#Produce graph for the drawing board
from turtle import *
#Set up the position to zero
setpos(0,0)
#Produce the x axis
goto(180,0)
goto(0,0)
#Produce the y axis
goto(0,150)
goto(0,0)
#Plot the data
month= [1,2,3,4,5,6,7,8,9,10,11,12]
sales= [120,110,80,66,66,45,40,20,45,75,95,130]
for i in range(len(sales)):
    goto(month[i]*15,sales[i])
    dot(5,"red")
    write(month[i], False, "center", "bold")
#Hide the turtle prompt
ht()
