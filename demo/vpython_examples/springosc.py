from visual import *

g = 9.8             #重力加速度 9.8 m/s^2
size = 0.05         #球半徑 0.05 m
r = 0.5             #彈簧原長 0.5m
k = 10              #彈簧力常數 10 N/m
m = 0.1             #球質量 0.1 kg

scene = display(width=800, height=800, center=(0, -r*0.6, 0), background=(0.5,0.5,0))  #設定畫面
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue)                    #畫天花板
ball = sphere(radius = size,  color=color.red)                              #畫球
spring = helix(radius=0.02, thickness =0.01)                                #畫彈簧,一端在(0,0,0)

ball.pos0 = vector(0, -r, 0)        #彈簧原長時，球的位置
ball.pos = vector(0, -r , 0)        #球初位置
ball.v = vector(0, 0, 0)            #球初速

dt = 0.001   
while True:
    rate(1000)
    spring.axis = ball.pos - spring.pos

    ball.a = vector(0, - g - k * (ball.pos.y - ball.pos0.y )/m , 0)

    ball.v +=   ball.a*dt
    ball.pos += ball.v*dt




