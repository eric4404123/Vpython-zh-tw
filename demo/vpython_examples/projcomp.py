from visual import *
g=9.8               #重力加速度 9.8 m/s^2
size = 0.25         #球半徑 0.25 m
air_drag_coe = 0.2  #空氣阻力系數


scene = display(title='拋體運動', width=1200, height=800, background=(0.5,0.5,0))#設定畫面
floor = box(length=50, height=0.01, width=4, color=color.blue)                  #畫地板
ball = sphere(radius = size,  color=color.red, make_trail = True)          #畫球
balla = sphere(radius = size,  color=color.blue, make_trail = True)

ball.pos = vector( -25.0, size, 0.0)    #球初始位置
ball.v = vector(10.0, 15.0 , 0.0)       #球初速

balla.pos = vector( -25.0, size, 0.0)    #球初始位置
balla.v = vector(10.0, 15.0 , 0.0)       #球初速

dt = 0.001                      #時間間隔 0.001秒
while ball.pos.y >= size:       #模擬直到球落地 即y=球半徑
    rate(1000)                   #每一秒跑1000次
    
    ball.pos += ball.v*dt
    ball.v += vector(0,- g*dt,0) 

while balla.pos.y >= size:       #模擬直到球落地 即y=球半徑
    rate(1000)                   #每一秒跑1000次
    
    balla.pos += balla.v*dt
    balla.v += vector(0,- g*dt,0) - air_drag_coe * balla.v * dt



       
                                         
           
