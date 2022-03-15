from visual import *
#needs a code clean-up (seems to now work on Python 2.4/VPython 3.2.9) 

print ("""
Electromagnetism: Ampere Law (v2.76) 2008-02-29
Rob Salgado (salgado@physics.syr.edu)

Electric Field vectors are blue. Magnetic Field vectors are red.

  The thick yellow vector representing
d|E|/dt ("time-rate-of-change-of-the-magnitude-of-the-electric-field")
is associated with the spatial arrangement of the magnetic field according to
the AMPERE-MAXWELL Law (as evaluated on the yellow loop).
[The sense of circulation on the yellow loop (by the RightHandRule) determines
the direction of change of the electric field... determined by your thumb.]

      CLICK the mouse to start and stop the animation
      TOGGLE: (a)mpere     (i) current (e) time-varying-E  
              (d)im-fields (n) color-scheme
              (c)alculus   (v)erbose""")

scene=display(
    width=800,height=600,
    x=0, y=0,
    title="Maxwell-Ampere v2.76 (Rob Salgado)")

colorScheme=0          #key n (negative)
colorBackground=[color.black,color.white]
colorCurrent=[color.white,color.orange]
colorBdimmed=[(0.4,0,0),(1,0.5,0.5)]

scene.ambient=0.4
Bcolor=[color.red,(1,0.5,0.5),color.yellow]
Bcolor[1]=colorBdimmed[colorScheme]
Icolor=colorCurrent[colorScheme]



scene.background=colorBackground[colorScheme]

scene.title="AMPERE: Currents and Changing-Es are associated with Curly-Bs"
scene.range=(2.5,2.5,2.5)
scene.forward=(-2.85804, -1.26038, -2.96742)

#scene.forward=(0.089623,4.193811,0.983082)

#scene.range=(1.5,1.5,1.5)
#scene.forward=(-2.85804, -1.26038, -2.96742)



showAmpere=0
showCurrent=1
showE=1
dimFields=0



E=[]
E.append( arrow(pos=vector(0.25,0,0),axis=vector(0,0,1e-3), shaftwidth=0.04,fixedwidth=1, color=color.blue)  )
E.append( arrow(pos=vector(-0.25,0,0),axis=vector(0,0,1e-3),shaftwidth=0.04,fixedwidth=1, color=color.blue)  )  
E.append( arrow(pos=vector(0,0.25,0),axis=vector(0,0,1e-3), shaftwidth=0.04,fixedwidth=1, color=color.blue)  )
E.append( arrow(pos=vector(0,-0.25,0),axis=vector(0,0,1e-3), shaftwidth=0.04,fixedwidth=1, color=color.blue)  )  
E.append( arrow(pos=vector(0.25,0,-2),axis=vector(0,0,1e-3), shaftwidth=0.04,fixedwidth=1, color=color.blue)  )
E.append( arrow(pos=vector(-0.25,0,-2),axis=vector(0,0,1e-3),shaftwidth=0.04,fixedwidth=1, color=color.blue)  )  
E.append( arrow(pos=vector(0,0.25,-2),axis=vector(0,0,1e-3), shaftwidth=0.04,fixedwidth=1, color=color.blue)  )
E.append( arrow(pos=vector(0,-0.25,-2),axis=vector(0,0,1e-3), shaftwidth=0.04,fixedwidth=1, color=color.blue)  )  


N=8
dEdt=current=0.2
B=[]
Bbox=[]  #clickable stems


for z in [0]:
    for r in [0.5]:
        for i in arange(0,N):
            theta=2.*pi*i/N
            theta_hat=vector(-sin(theta), cos(theta), 0) 
            Bfield=current*theta_hat/r
            A=arrow(pos=vector(r*cos(theta),r*sin(theta),z) , axis=Bfield,shaftwidth=0.04,fixedwidth=1,color=color.red)
            B.append(A)
            Bbox.append( box(pos=A.pos+A.axis/4.,axis=A.axis,length=mag(A.axis)/2.,height=0.04,width=0.04,color=color.red) )
    for r in [1,1.5]:
        for i in arange(0,N):
            theta=2.*pi*i/N
            theta_hat=vector(-sin(theta), cos(theta), 0) 
            Bfield=current*theta_hat/r
            A=arrow(pos=vector(r*cos(theta),r*sin(theta),z) , axis=Bfield,shaftwidth=0.04,fixedwidth=1,color=color.red)
            B.append(A)
            Bbox.append( box(pos=A.pos+A.axis/4.,axis=A.axis,length=mag(A.axis)/2.,height=0.04,width=0.04,color=color.red) )

for z in [-0.5,0.5,-1,1]:
    for r in arange (.5,1.5,.5):
        for i in arange(0,N):
            theta=2.*pi*i/N
            theta_hat=vector(-sin(theta), cos(theta), 0) 
            Bfield=current*theta_hat/r
            A=arrow(pos=vector(r*cos(theta),r*sin(theta),z) , axis=Bfield,shaftwidth=0.04,fixedwidth=1,color=color.red)
            B.append(A)
            Bbox.append( box(pos=A.pos+A.axis/4.,axis=A.axis,length=mag(A.axis)/2.,height=0.04,width=0.04,color=color.red) )



hcolor=Bcolor[2]

Ep=[]
for e in E:
    Ep.append( arrow(pos=e.pos+e.axis,axis=dEdt*norm(e.axis),
                     #length=dEdt,
                     fixedwidth=1, color=hcolor, shaftwidth=0.07,headwidth=0.14, visible=showAmpere*showE)  )  


Bloop_rad=mag(B[0].pos)
AmpereLoop=curve(color=hcolor, x=Bloop_rad*cos(2.*pi*arange(40)/40.), y=Bloop_rad*sin(2.*pi*arange(40)/40.), visible=showAmpere )

 



I=cylinder(radius=0.04,pos=vector(0,0,-2),axis=vector(0,0,4), color=Icolor)
chgpos=[]
chg=[]
for i in arange(0,N):
    chgpos.append(vector(I.pos+I.axis*i/N))
    chg.append(sphere(pos=chgpos[-1],radius=0.06,color=I.color))

   
    
t=9.50
#t=10.0
#t=10.5
dt=0
dt=1

#Now... WHEN AN OBJECT IS PICKED,
#TRANSLATE THE scene.center TO THE OBJECT'S POSITION        
while 1:
    rate(10)
    #print scene.forward
    t += dt
    for i in arange(0,N):
        chg[i].pos = chgpos[i]+(t%4)*vector(0,0,.125)
    ecount=0
    for e in E:
        e.length = (t%20)/10.+1e-3
        Ep[ecount].pos=e.pos+e.axis; ecount +=1
        
        
    if scene.mouse.clicked:
        scene.mouse.getclick()
        newPick=scene.mouse.pick
        if newPick !=None:
            ### ANIMATE TO SELECTED POSITION
            tempcolor=newPick.color
            newPick.color=color.yellow
            target=newPick.pos
            step=(target-scene.center)/20.
            for i in arange(1,20,1):
                rate(10)
                scene.center +=step
                scene.scale *= 1.037  #(1.037**19=1.99)
            newPick.color=tempcolor

    if scene.kb.keys: # is there an event waiting to be processed?
        s = scene.kb.getkey() # obtain keyboard information
        if s=='a':
            showAmpere +=1; showAmpere %=2; AmpereLoop.visible=showAmpere
            for i in Ep:
                i.visible=showAmpere*showE

            if showAmpere==1:
                for i in arange(0,N):
                    B[i].color=hcolor
                    Bbox[i].color=hcolor
            else:
                for i in arange(0,N):
                    B[i].color=color.red
                    Bbox[i].color=color.red

        if s=='d':
            dimFields +=1; dimFields %=2; 

            for i in arange(N,len(B)):
                B[i].color=Bcolor[dimFields]
                Bbox[i].color=Bcolor[dimFields]
            for i in arange(1,4*N+1):
                B[-i].visible=(1-dimFields)
                Bbox[-i].visible=(1-dimFields)

        if s=='i':
            showCurrent +=1; showCurrent %=2; 
            I.visible=showCurrent
            for i in chg: i.visible=showCurrent
            
        if s=='e':
            showE +=1; showE %=2;
            for e in E: e.visible=showE
            for e in Ep: e.visible=showE*showAmpere
            

        if s=='n':
            colorScheme = (colorScheme+1)%2 #TOGGLE colorScheme
            scene.background=colorBackground[colorScheme]
            Bcolor[1]=colorBdimmed[colorScheme]
            Icolor=colorCurrent[colorScheme]; I.color=Icolor
            scene.background=colorBackground[colorScheme]

            for i in arange(N,len(B)):
                B[i].color=Bcolor[dimFields]
                Bbox[i].color=Bcolor[dimFields]
            for i in arange(1,4*N+1):
                B[-i].visible=(1-dimFields)
                Bbox[-i].visible=(1-dimFields)
            for c in chg:
                c.color=Icolor        
            
            #dEdtlabel.opacity=labelBackground[colorScheme]
            #dBdtlabel.opacity=labelBackground[colorScheme]
            #ddtcolor[0]=Bcolor[2+colorScheme]
            #ddtcolor[1]=Ecolor[2+colorScheme]

        if s=='z':
            print ("scene.center=(%f,%f,%f)"  % tuple(scene.center))
            print ("scene.forward=(%f,%f,%f)"  % tuple(scene.forward))
            print ("scene.range=(%f,%f,%f)"  % tuple(scene.range))
            print ("t=%f\n" %t)

        if s==' ':
            dt  +=1; dt %=2; 