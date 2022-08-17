#random number generator
import random
#time thing to run the loop at set interval
import time
#imports os to clear the terminal
import os

from pytimedinput import timedInput

#bool to stop if you die
gameOver = bool(False)
#map width
width = int(80)
#map height
height = int(20)
#coordinates for snake
x = int
y = int
#fruit coordinates
fruitX = int
fruitY = int
#score
score = int

something = ""

timer = int(0)

#direction bools
upwards = bool(False)
downwards = bool(False)
leftwards = bool(False)
rightwards = bool(False)

def setup():
    #gameover bool
    global gameOver
    gameOver = False
    #coordinate in the middle of the map for snake spawn
    global x
    x = width / 2
    global y
    y = height / 2
    #randomly generate fruit spawn coordinate
    global fruitX
    fruitX = random.randrange(1, width)
    global fruitY
    fruitY = random.randrange(1, height)
    #score int
    global score
    score = 0


#draw the graphics
def draw():
    print("snaek gaem")
    
    #draw top horizontal wall
    for i in range(width+2):
        #(, end="") disables endline, while print("") acts as endline
        print("#", end="")
    print("")
    
    #draw side walls
    for i in range(height):
        for j in range(width):
            #print left wall
            if j == 0: print("#", end="")
            #print snake in center
            if i == y and j == x: print("O", end="")
            #print fruit in random position
            elif i == fruitY and j == fruitX: print("F", end="")
            #print nothing if empty space
            else: print(" ", end="")
            #print right wall
            if j == width-1: print("#", end="")  
        print("")
    
    #draw bottom horizontal wall
    for i in range(width+2):
        print("#", end="")
    #prints score
    print("")
    print("")
    print("score: ", score)
    
    global timer
    timer = timer + 1
    print(timer)
    print(something)
        



def logic():
    global x
    global y
    
    if something == "": x = x + 1
    
    if something == "w": y = y - 1
    if something == "s": y = y + 1
    if something == "a": x = x - 1
    if something == "d": x = x + 1
    




def main():
    setup()
    global something
    global x
    global y
    while gameOver is False:
        os.system('cls')  
        draw()
        logic()
        txt,_ = timedInput('get input:', timeout = 0.05)
        match txt:
            case 'w': something = "w"
            case 's': something = "s"
            case 'a': something = "a"
            case 'd': something = "d"
main()