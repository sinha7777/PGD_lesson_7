import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

stars = []
number_of_stars = 2        
next_stars = 0

level = 1                  

start_time = 0
total_time = 0

lines = []

def create_stars():
    global start_time, stars, lines, next_stars
    stars = []
    lines = []
    next_stars = 0

    for i in range(number_of_stars):
        star = Actor("star")
        star.pos = randint(50, 750), randint(50, 550)
        stars.append(star)

    start_time = time()

create_stars()

def draw():
    global total_time
    screen.blit("space", (0, 0))


    number = 1
    for star in stars:
        star.draw()
        screen.draw.text(str(number), (star.pos[0], star.pos[1] + 20))
        number += 1


    for line in lines:
        screen.draw.line(line[0], line[1], (255, 255, 255))


    total_time = time() - start_time
    screen.draw.text("Time: " + str(round(total_time, 1)), (10, 10), fontsize=30)


    screen.draw.text("Level: " + str(level), (10, 50), fontsize=30, color="yellow")


    if next_stars == number_of_stars:
        screen.draw.text("Level Complete!", (250, 300), fontsize=60, color="white")

def update():
    pass

def on_mouse_down(pos):
    global next_stars, lines, number_of_stars, level

    if next_stars < number_of_stars:
        if stars[next_stars].collidepoint(pos):
            if next_stars:
                lines.append((stars[next_stars - 1].pos, stars[next_stars].pos))
            next_stars += 1
        else:
            next_stars = 0
            lines = []


    if next_stars == number_of_stars:
        level += 1
        number_of_stars += 1      
        create_stars()            

pgzrun.go()
