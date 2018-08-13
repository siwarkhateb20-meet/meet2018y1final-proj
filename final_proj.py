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
turtle.write("hi, "+name,move=False,align="center",font=("Arial",30))
turtle.ht()

ready = input("are you ready!? >_<")
if ready == "yes" :
    bottle.goto(0,50)
    bottle.ht()
####### WRITE THE Q/A's HERE!  :



answer1 = input("3+3?")

if answer1 == '6':
    correct =True
else:
    correct = False










    ######################################################################################

new_bottle = turtle.clone()
turtle.register_shape('/home/student/siwarkhateb20_final-proj/meet2018y1final-proj/ezgif-4-1105f2a5f5 (1).gif')
bottle.shape("/home/student/siwarkhateb20_final-proj/meet2018y1final-proj/ezgif-4-1105f2a5f5 (1).gif")
if correct:
   
    bottle.showturtle()
bottle.penup()
bottle.goto(-400,70)
bottle.showturtle()
    
