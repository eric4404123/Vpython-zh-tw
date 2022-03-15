from visual import *

ball = sphere(pos=(-5,0,0), radius=0.5, color=color.red)
wall = box(pos=(6,0,0), size=(0.2,4,4), color=color.green)
ball.velocity = vector(2,0,0)

while (1==1):
    rate(100) # 設定速度 1/100 秒
    dt = 0.05 # 設定間隔
    ball.pos = ball.pos + ball.velocity*dt
    if ball.x > wall.x:
        ball.velocity.x = -ball.velocity.x # 撞牆的設定
