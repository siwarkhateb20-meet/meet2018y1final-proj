import turtle
import random
import time

'''
def stop(x,y):
    print('function')
    global run
    run=False

run = True
while run:
    print(run)
    turtle.onclick(stop)
    turtle.listen()
'''
#music
from pygame import mixer # Load the required library
mixer.init()



    
#firs bottle
bottle = turtle.clone()
turtle.register_shape('used_waterbottle.gif')
bottle.shape("used_waterbottle.gif")

#the machine
screen = turtle.Screen()
screen.setup(1000,1000)
screen.bgpic('machine1.gif')
bottle.ht()
bottle.penup()
bottle.speed(1)
bottle.goto(400,50)
bottle.showturtle()
#ENTER YOUR NAME
name = turtle.textinput("","enter your name plz ")

if name == "caleb" :
    turtle.up()
    turtle.goto(0,400)
    turtle.down()
    turtle.write( str(name)  +"you are the best instructor evveer, we love you!!",move=False,align="center",font=("Arial",30))
    turtle.stamp()
    turtle.ht()


if name != "caleb" :
    turtle.up()
    turtle.goto(0,400)
    turtle.down()
    turtle.write("hey ," + name ,move=False,align="center",font=("Arial",30))
    turtle.stamp()
    turtle.ht()



ready = turtle.textinput("","are you ready!? >_<")
if ready == "yes" :
    bottle.goto(150,50)
    bottle.ht()

elif ready == "no" :
    turtle.clear()
    turtle.write("we dont care, you have to play",move=False,align="center",font=("Arial",30))
    bottle.goto(150,50)
    bottle.ht()

##################################################################################################################################

bottles = 0
correct_answers = 0


# the first question:

answer = turtle.textinput("Title","how many trees are cut down each day for toilet paper?, A = 50,000 , B = 20,250 , C = 27,000 , D = 150,000 ")
if answer == "A" or answer == "a":

    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was C")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer == "B" or answer == "b":

    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was C")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer == "C" or answer == "c" :
    
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("green")
    turtle.clear()
    turtle.write("correct",font=("Arial",30))
    print("correct")
    mixer.music.load('correct.mp3')
    mixer.music.play()
    bottles += 1
    correct_answers += 1
    
elif answer == "D" or answer == "d":
    
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was C")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()

# the secound question:

answer1 = turtle.textinput("Title","how much time does it take for a glass bottle to decompose? A = 100 years, B = 4,000 years, C = 37,000 years, D = 2,500 years ")
if answer1 == "A" or answer1 == "a":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was B")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer1 == "B" or answer1 == "b":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("green")
    turtle.clear()
    turtle.write("correct",font=("Arial",30))
    print("correct")
    mixer.music.load('correct.mp3')
    mixer.music.play()
    bottles += 1
    correct_answers += 1

elif answer1 == "C" or answer1 == "c":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was B")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer1 == "D" or answer1 == "d":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was B")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()

#the third question:

answer2 = turtle.textinput("Title"," only ______% of our planet's water are fresh. A = 3%, B = 1%, c = 15%, D = 37% ")
if answer2 == "A" or answer2 == "a":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("green")
    turtle.clear()
    turtle.write("correct",font=("Arial",30))
    print("correct")
    mixer.music.load('correct.mp3')
    mixer.music.play()
    bottles += 1
    correct_answers += 1
    
elif answer2 == "B" or answer2 == "b":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print(" incorrect , the rght answer was A ")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer2 == "C" or answer2 == "c" :
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print(" incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer2 == "D" or answer2 == "d":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print(" incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()

# the forth question:

answer3 = turtle.textinput("Title"," how many people don't have accsess to clean water? A = 700M, B = 430M, C = 100M, D = 30M")
if answer3 == "A" or answer3 == "a":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("green")
    turtle.clear()
    turtle.write("correct",font=("Arial",30))
    print( "correct")
    mixer.music.load('correct.mp3')
    mixer.music.play()
    bottles += 1
    correct_answers += 1

elif answer3 == "B" or answer3 == "b":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print(" incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()


elif answer3 == "C" or answer3 == "c" :
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print(" incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer3 == "D" or answer3 == "d":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()

# the fifth question:

answer4 = turtle.textinput("Title"," who is the num_1 trash producer in the world? A = japan, B = US_of_A, C = china, D = India ")

if answer4 == "A" or answer4 == "a":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print( " incorrect , the rght answer was B")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer4 == "B" or answer4 == "b":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("green")
    turtle.clear()
    turtle.write("correct",font=("Arial",30))
    print("correct")
    mixer.music.load('correct.mp3')
    mixer.music.play()
    bottles += 1
    correct_answers += 1

elif answer4 == "C" or answer4 == "c" :
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was B")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer4 == "D" or answer4 == "d":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was B")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()

# the sixth question:

answer5 = turtle.textinput("Title"," americans use _______ platic bottles in a single hour. A = 2,500,000, B = 1,000,000, C = 750,000, D = 100,000")

if answer5 == "A" or answer5 == "a":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("green")
    turtle.clear()
    turtle.write("correct",font=("Arial",30))
    print( "correct")
    mixer.music.load('correct.mp3')
    mixer.music.play()
    bottles += 1
    correct_answers += 1

elif answer5 == "B" or answer5 == "b":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()

elif answer5 == "C" or answer5 == "c" :
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()
    
elif answer5 == "D" or answer5 == "d":
    turtle.pu()
    turtle.goto(-100,80)
    turtle.pencolor("red")
    turtle.clear()
    turtle.write("incorrect",font=("Arial",30))
    print("incorrect , the rght answer was A")
    mixer.music.load('incorrect.mp3')
    mixer.music.play()


#####################################################################################################################################
#secend bottle
correct = True
incorrect = False
offset = 0
turtle.register_shape('/home/student/siwarkhateb20_final-proj/meet2018y1final-proj/ezgif-4-1105f2a5f5 (1).gif')
bottle.shape("/home/student/siwarkhateb20_final-proj/meet2018y1final-proj/ezgif-4-1105f2a5f5 (1).gif")
for i in range(bottles):
    new_bottle = turtle.clone()
    bottle.speed(1)
    bottle.goto(-70,70)
    
    bottle.showturtle()
    bottle.penup()
    bottle.goto(-400+offset,70)
    offset += 30
    
    bottle.ht()
    bottle.stamp()

turtle.goto(0,300)

turtle.pencolor("blue")
turtle.write("You answered " + str(correct_answers) + " / 6 correct answers" ,align ="center",font=("Arial", 24))

time.sleep(2)

if bottles == 6 :
    turtle.register_shape("c.gif")
    #turtle.clear()
    #turtle.showturtle()
    congrats = turtle.clone()
    congrats.st()
    congrats.goto(0,450)
    congrats.shape('c.gif')

print(bottles)
if bottles == 0 :
    turtle.register_shape("try_again.gif")
    try_again = turtle.clone()
    try_again.st()
    try_again.goto(0,430)
    try_again.shape('try_again.gif')
    
        
turtle.mainloop()

