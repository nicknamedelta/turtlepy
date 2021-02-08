#!/usr/bin/env python3
import os, turtle
from random import randrange
from PIL import Image

MAX_ANGLE = 30
MAX_DISTANCE = 250

# base colors
colors = ['aqua', 'red', 'purple', 'blue', 'green', 'yellow', 'orange']
colorss = ['gray', 'white']

def draw(op, name):
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    if op == 1:
        for x in range(180):
            turtle.pencolor(colorss[x%2])
            turtle.width(x/100+1)
            turtle.forward(x)
            turtle.right(80)
    elif op == 2:
        for x in range(100):
            turtle.pencolor(colorss[x%2])
            turtle.width(x/100+1)
            turtle.forward(x)
            turtle.left(170)
    elif op == 3:
        for angle in range(0, 360, 2):
            turtle.penup()
            turtle.home()
            turtle.pendown()
            turtle.setheading(angle)

            while turtle.distance(0, 0) < MAX_DISTANCE:
                turtle.pencolor(colorss[angle%2])
                angle = randrange(-MAX_ANGLE, MAX_ANGLE + 1)
                turtle.right(angle)
                turtle.forward(50)
    elif op == 4:
        for x in range(100):
            turtle.width(x/100+1)
            for y in range(20):
                turtle.pencolor(colorss[x%2])
                turtle.forward(0.5+10+y)
                turtle.left(77 / 9)
            turtle.left(77)
    elif op == 5:
        for x in range(180):
            turtle.width(x/100+1)
            for y in range(6):

                turtle.pencolor(colorss[x%2])
                turtle.forward(x/6)
                turtle.left(40)
            turtle.left(100)
            # turtle.dot(6)
    elif op == 6:
        for x in range(200):
            turtle.pencolor(colorss[x%2])
            turtle.forward(x*2)
            turtle.right(121)
    elif op == 7:
        size = 1
        for x in range(50):
            for y in range(4):
                turtle.pencolor(colorss[x%2])
                turtle.forward(size+y-1)
                turtle.right(90)
            size += 1
            turtle.right(10)
    elif op == 8:
        for x in range(360):
            turtle.pencolor(colorss[x%2])
            turtle.forward(x)
            turtle.right(91)

    # convert draw in image
    img_canvas = turtle.getscreen().getcanvas()
    save_as_png(img_canvas, name)

    # wait user close the draw
    turtle.done()


def save_as_png(canvas, fileName):
    # save postscript image 
    canvas.postscript(file = fileName + '.eps')

    # open an eps image 
    img = Image.open(fileName + '.eps')

    # will convert image color to RGB
    fig = img.convert('RGB')

    # convert eps to png
    fig.save(fileName + '.png', lossless = True)
    
    # remove .eps file
    if os.path.exists(fileName + '.eps'):
        os.remove(fileName + '.eps')
    else:
        print('.eps file unknown')

    print('(｡^‿^｡) - "Your image has been generated!"')

def main():
    print('(｡^‿^｡) - "What should I draw today?":\n')
    print('1 - spiral\n2 - star\n3 - flower\n4 - leafs\n5 - unknown\n6 - triangle\n7 - shell\n8 - square\n0 - exit')

    fileNames = ['turtlepyspiral', 'turtlepystar', 'turtlepyflower', 'turtlepyleafs', 'turtlepyunknown', 'turtlepytriangle', 'turtlepyshell', 'turtlepysquare']
    sOp = int(input())

    if (sOp >= 1 and sOp <=8):
        draw(sOp, fileNames[sOp-1])
    if (sOp == 0):
        exit()
    else:
        print('(⋟﹏⋞) - "sorry, i can\'t make this."')
main()
