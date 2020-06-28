#!/usr/bin/env python3
import turtle
from random import randrange
from PIL import Image

MAX_ANGLE = 30
MAX_DISTANCE = 250

# base colors
colors = ['aqua', 'red', 'purple', 'blue', 'green', 'yellow', 'orange']
colorss = ['gray', 'white']

def rainbow_spiral():
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    for x in range(180):
        # turtle.pencolor(colors[x%7])
        turtle.pencolor(colorss[x%2])
        turtle.width(x/100+1)
        turtle.forward(x)
        turtle.right(80)

    turtle.done()
        
def rainbow_star():
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    for x in range(100):
        # turtle.pencolor(colors[x%7])
        turtle.pencolor(colorss[x%2])
        turtle.width(x/100+1)
        turtle.forward(x)
        turtle.left(170)

    turtle.done()


def rainbow_flower():
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    for angle in range(0, 360, 2):
        turtle.penup()
        turtle.home()
        turtle.pendown()
        turtle.setheading(angle)

        while turtle.distance(0, 0) < MAX_DISTANCE:
            # turtle.pencolor(colors[angle%7])
            turtle.pencolor(colorss[angle%2])
            angle = randrange(-MAX_ANGLE, MAX_ANGLE + 1)
            turtle.right(angle)
            turtle.forward(50)

    turtle.done()

def rainbow_leafs():
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    for x in range(100):
        turtle.width(x/100+1)
        for y in range(20):
            # turtle.pencolor(colors[x%7])
            turtle.pencolor(colorss[x%2])
            turtle.forward(0.5+10+y)
            turtle.left(77 / 9)
        turtle.left(77)

    turtle.done()

def rainbow_unknown():
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    for x in range(180):
        turtle.width(x/100+1)
        for y in range(6):
            # turtle.pencolor(colors[x%7])
            turtle.pencolor(colorss[x%2])
            turtle.forward(x/6)
            turtle.left(40)
        turtle.left(100)
        # turtle.dot(6)

    turtle.done()

def save_as_png(canvas, fileName):
    # save postscipt image 
    canvas.postscript(file = fileName + '.eps')

    # open an eps image 
    img = Image.open(fileName + '.eps')

    # will convert image color to RGBA
    fig = img.convert('RGB')

    # convert eps to png
    fig.save(fileName + '.png', lossless = True)

    print('(｡^‿^｡) - "your image has been generated!"')

def main():
    print('(｡^‿^｡) - "what i should draw today ?":\n')
    print('1 - Spiral\n2 - Star\n3 - flower\n4 - leafs\n5 - unknown')

    ans = int(input())

    if ans == 1:
        fileName = 'turtlepyspiral'
        rainbow_spiral()
    elif ans == 2:
        fileName = 'turtlepystar'
        rainbow_star()
    elif ans == 3:
        fileName = 'turtlepyflower'
        rainbow_flower()
    elif ans == 4:
        fileName = 'turtlepyleafs'
        rainbow_leafs()
    elif ans == 5:
        fileName = 'turtlepyunknown'
        rainbow_unknown()
    else:
        print('(⋟﹏⋞) - "sorry, i can\'t make this."')

    # convert draw in image
    img_canvas = turtle.getscreen().getcanvas()
    save_as_png(img_canvas, fileName)

main()
