import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=600

satellites = []
number_of_satellites = 8
next_satellites = 0

start_time = 0
end_time = 0
total_time = 0

lines = []

def create_satellites():
    global start_time
    for i in range(number_of_satellites):
        satellite = Actor("satellites")
        satellite.pos = randint(50,750) , randint(50,550)
        satellites.append(satellite)
    start_time = time()

create_satellites()

def draw():
    global total_time
    screen.blit("space",(0,0))

    number = 1

    for satellite in satellites :
        satellite.draw()
        screen.draw.text(str(number),(satellite.pos[0],satellite.pos[1]+20))
        number += 1

    for line in lines:
        screen.draw.line(line[0],line[1],(255,255,255))

    if next_satellites < number_of_satellites:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)
    
    else:
        screen.draw.text(str(round(total_time,1)),(10,10),fontsize=30)

    if next_satellites == number_of_satellites:
        screen.draw.text("good job you won.",(250,300),fontsize=60,color="white")

def update():
    pass

def on_mouse_down(pos):
    global next_satellites
    global lines
    if next_satellites < number_of_satellites:
        if satellites[next_satellites].collidepoint(pos) :
            if next_satellites:
                lines.append((satellites[next_satellites-1].pos, satellites[next_satellites].pos))
            next_satellites += 1
        else:
            next_satellites = 0
            lines = []  

pgzrun.go()