import turtle
import random

bottle = turtle.clone()
turtle.register_shape('used_waterbottle.gif')
bottle.shape("used_waterbottle.gif")


screen = turtle.Screen()
screen.setup(1000,1000)
screen.bgpic('machine1.gif')
bottle.ht()
bottle.penup()
bottle.goto(400,50)
bottle.showturtle()

name = input("inter your name plz ")
turtle.up()
turtle.goto(0,400)
turtle.down()
turtle.write(name,move=False,align="center",font=("Arial",30))
turtle.ht()

ready = input("are you ready!? >_<")
if ready == "yes" :
    bottle.goto(0,50)
    
'''
bottles = turtle.clone()

turtle.register_shape('water_bottles.gif')

bottles.shape('water_bottles.gif')
'''

