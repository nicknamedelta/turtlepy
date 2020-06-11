#!/usr/bin/env python3
import turtle
from PIL import Image

# base colors
colors = ['aqua', 'red', 'purple', 'blue', 'green', 'yellow', 'orange']

def rainbow_spiral():
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    for x in range(360):
        turtle.pencolor(colors[x%7])
        turtle.width(x/100+1)
        turtle.forward(x)
        turtle.left(70)
        
def rainbow_star():
    # background, speed and hide pen while draw
    turtle.bgcolor('black')
    turtle.speed('fastest')
    turtle.hideturtle()

    for x in range(360):
        turtle.pencolor(colors[x%7])
        turtle.width(x/100+1)
        turtle.forward(x)
        turtle.left(170)

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
    print('1 - Spiral\n2 - Star')

    ans = int(input())

    if ans == 1:
        fileName = 'turtlepyspiral'
        rainbow_spiral()
    elif ans == 2:
        fileName = 'turtlepystar'
        rainbow_star()
    else:
        print('(⋟﹏⋞) - "sorry, i can\'t make this."')

    # convert draw in image
    img_canvas = turtle.getscreen().getcanvas()
    save_as_png(img_canvas, fileName)

main()