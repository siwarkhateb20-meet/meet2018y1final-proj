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
#############################################################


# the first question:

answer = input("how many trees are cut down each day for toilet paper?, A = 50,000 , B = 20,250 , C = 27,000 , D = 150,000 ")
if answer == "A" or answer == "a":
    print( " you wish!")
elif answer == "B" or answer == "b":
    print(" optimistic haa?")
elif answer == "C" or answer == "c" :
    print(" finally , a real tree hugger")
elif answer == "D" or answer == "d":
    print(" wow, slow down champ")

# the secound question:

answer1 = input("how much time does it take for a glass bottle to decompose? A = 100 years, B = 4,000 years, C = 37,000 years, D = 2,500 years ")
if answer1 == "A" or answer1 == "a":
    print( " wake up! globale warming is real!")
elif answer1 == "B" or answer1 == "b":
    print(" thats right doggggggg")
elif answer1 == "C" or answer1 == "c":
    print(" what the hell bro???")
elif answer1 == "D" or answer1 == "d":
    print(" sorry dude")

#the third question:

answer2 = input(" only ______% of our planet's water are fresh. A = 3%, B = 1%, c = 15%, D = 37% ")
if answer2 == "A" or answer2 == "a":
    print( " you get water! yay. you know, there are people in africa with no access to clean water, still happy? you monster!  ")
elif answer2 == "B" or answer2 == "b":
    print(" you just killed half of the world population! ")
elif answer2 == "C" or answer2 == "c" :
    print(" have you seen the kineret??!")
elif answer2 == "D" or answer2 == "d":
    print(" you must be very stupid")

# the forth question:

answer3 = input(" how many people don't have accsess to clean water? A = 700M, B = 430M, C = 100M, D = 30M")
if answer3 == "A" or answer3 == "a":
    print( " reality is sad, you can change it, so please do!")
elif answer3 == "B" or answer3 == "b":
    print(" yasssss == False")
elif answer3 == "C" or answer3 == "c" :
    print(" you are a rap god! so stick to rapping")
elif answer3 == "D" or answer3 == "d":
    print(" maybe one day")

# the fifth question:

answer4 = input(" who is the num_1 trash producer in the world? A = japan, B = US_of_A, C = china, D = India ")
if answer4 == "A" or answer4 == "a":
    print( " Anata wa anata no kazoku ni totte wa hazukashi")
elif answer4 == "B" or answer4 == "b":
    print(" the age of trump is starting to show its effects on the USA")
elif answer4 == "C" or answer4 == "c" :
    print(" are a trump voter?")
elif answer4 == "D" or answer4 == "d":
    print(" thats racist!")

# the sixth question:

answer5 = input(" americans use _______ platic bottles in a single hour. A = 2,500,000, B = 1,000,000, C = 750,000, D = 100,000")
if answer5 == "A" or answer5 == "a":
    print( "paris agrrements, who needs 'em?")
elif answer5 == "B" or answer5 == "b":
    print(" B is your score. proud?")
elif answer5 == "C" or answer5 == "c" :
    print(" thats wrong y'all (caleb wrote this - he asked me to say yaaaaaaaaaaassssss for him.) ")
elif answer5 == "D" or answer5 == "d":
    print(" D stands for DON'T") 


#############################################################
new_bottle = turtle.clone()
turtle.register_shape('/home/student/siwarkhateb20_final-proj/meet2018y1final-proj/ezgif-4-1105f2a5f5 (1).gif')
bottle.shape("/home/student/siwarkhateb20_final-proj/meet2018y1final-proj/ezgif-4-1105f2a5f5 (1).gif")
if correct:
   
    bottle.showturtle()
bottle.penup()
bottle.goto(-400,70)
bottle.showturtle()
    
