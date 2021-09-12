print("""\n\n\n
 _____                       ______              _____                      
/  ___|                      | ___ \            |  __ \                     
\ `--. _ __   __ _  ___ ___  | |_/ / __ _ _ __  | |  \/ __ _ _ __ ___   ___ 
 `--. \ '_ \ / _` |/ __/ _ \ | ___ \/ _` | '__| | | __ / _` | '_ ` _ \ / _ \
/\__/ / |_) | (_| | (_|  __/ | |_/ / (_| | |    | |_\ \ (_| | | | | | |  __/
\____/| .__/ \__,_|\___\___| \____/ \__,_|_|     \____/\__,_|_| |_| |_|\___|
      | |                                                                   
      |_|                                                                   
\n\n\n""")
print("Created By AlPHA\n\n")


import time
import turtle
from turtle import *
import sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

print_slow("Importing Modules ...\n\n")

turtle.hideturtle()
turtle.up()
turtle.goto(-150,0)
screen = Screen()
screen.setup(500, 500)

start = 0
spacePress = 0
turtle.write("Press Left for Game 1 Right for Game 2", font=("Arial", 13, "normal"))

game1Playing = False
game1end = False

game2Playing = False
game2end = False
timerActive = False

ready = False

t1 = int(input("How much time?: \n"))
t2 = int(input("\nHow many spaces?: \n"))

ready = True

def left():
  global ready
  if (ready):
    global game1Playing
    global start
    game1Playing = True
    start = time.time()
    turtle.clear()
    turtle.goto(-100,0)
    turtle.write("Click Space as Much as Possible", font=("Arial", 13, "normal"))

def right():
  global ready
  if (ready):
    global game2Playing
    game2Playing = True
    turtle.clear()
    turtle.goto(-100,0)
    turtle.write("Click Space as Much as Possible", font=("Arial", 13, "normal"))


def TimerActivate():
  global t1
  global game2end
  timeVal = t1
  for i in range(timeVal):
    turtle.clear()
    turtle.goto(-100,0)
    turtle.write("Seconds Remaining: " + str(timeVal - i), font=("Arial", 13, "normal"))
    time.sleep(1)
  game2end = True
  game2Playing = False



def space():
  global t2
  global game1Playing
  global spacePress
  global timerActive
  global game2Playing
  spacePressAmt = t2
  if (game1Playing):
    spacePress+=1
    turtle.clear()
    end = time.time()
    turtle.goto(-50,0)
    turtle.write(str(spacePress) + "/" + str(spacePressAmt) + " presses", font=("Arial", 10, "normal"))

    if (spacePress >= spacePressAmt):
      end = time.time()
      print(end-start)
      turtle.clear()
      turtle.goto(-50,0)
      turtle.write("Time is " + str(round(end-start,2)) + " seconds!", font=("Arial", 10, "normal"))
      game1Playing = False
  elif (game2Playing):
    spacePress+=1
    if (timerActive == False):
      timerActive = True
      TimerActivate()
    if (game2end):
      turtle.clear()
      turtle.goto(-15,0)
      turtle.write(str(spacePress) + " Presses!", font=("Arial", 10, "normal"))
      game2Playing = False




turtle.onkey(space, "space")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.listen()
turtle.mainloop()