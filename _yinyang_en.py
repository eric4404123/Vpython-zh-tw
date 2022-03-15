#!/usr/bin/python
'''翻譯失敗，網路可能有問題！保留原文 ... 翻譯失敗，網路可能有問題！保留原文 ...        turtle-example-suite:

            tdemo_yinyang.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

'''

from turtle import *

def yin(radius, color1, color2):
    width(3)
    color("black", color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    lt(180)
    circle(-radius/2., 180)
    end_fill()
    lt(90)
    up()
    forward(radius*0.35)
    rt(90)
    pendown()
    color(color1, color2)
    begin_fill()
    circle(radius*0.15)
    end_fill()
    lt(90)
    up()
    bk(radius*0.35)
    pendown()
    lt(90)

def main():
    reset()
    yin(200, "black", "white")
    yin(200, "white", "black")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
