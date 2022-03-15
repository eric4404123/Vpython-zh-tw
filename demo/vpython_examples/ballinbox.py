from visual import *
ball = sphere(pos=(0,0,0), radius=0.5, color=color.cyan)
wallR = box(pos=(6,0,0), size=(0.2,12,12), color=color.green)
wallL = box(pos=(-6,0,0), size=(0.2,12,12), color=color.green)
wallfar = box(pos=(0,0,-6), size=(12,12,0.2), color=color.red)
wallU = box(pos=(0,6,0), size=(12,0.2,12), color=color.blue)
wallB = box(pos=(0,-6,0), size=(12,0.2,12), color=color.blue)
ball.velocity = vector(25,5,15)
deltat = 0.005
t = 0
ball.trail = curve(color = ball.color )
scene.autoscale = False
vscale = 0.1
varr=arrow (pos = ball.pos,axis=vscale*ball.velocity,color = color.yellow)


while t < 300:
    rate(24)
    if ball.pos.x > wallR.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.x < wallL.pos.x:
        ball.velocity.x = -ball.velocity.x
    if ball.pos.y > wallU.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.y < wallB.pos.y:
        ball.velocity.y = -ball.velocity.y
    if ball.pos.z > 6:
        ball.velocity.z = -ball.velocity.z
    if ball.pos.z < wallfar.pos.z:
        ball.velocity.z = -ball.velocity.z




    ball.pos = ball.pos + ball.velocity*deltat
    ball.trail.append(pos = ball.pos)
    t = t + deltat
    var.visible = 0