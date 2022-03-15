from visual import *


print("""
Interactive Superposition of Coherent Sources (ver 2/16/2004)
Rob Salgado (salgado@physics.syr.edu)
""")
### ver 2/16/2004   tested on Windows 2000
###                 with Python-2.3.3.exe and VPython-2003-10-05.exe
###                 Navigation needs work. The mouse should be able to
###                    drag each of the three points along the xz-plane.
###                    The relation between the dragged point and mouse
###                    cursor look unnatural.

#phase=arange(0,1,.1)
#print len(phase)
#sinphase=sin(phase)
#print phase, sinphase
#eqn =raw_input('formula')
#x=arange(0,10,0.1)
#c=curve(x=x,y=eval(eqn))

場景.autoscale=0
場景.range=(12,12,12)
場景.設標題="Wave Superposition"

t=0

AA=1
Ak=2.*pi/5
Aw=1
Ap=0

wavelength=2.*pi/Ak

Ax0=0; Ay0=0
Ax1=10;Ay1=0
Adx=Ax1-Ax0
Ady=Ay1-Ay0
Ar=arange(0,sqrt(Adx*Adx+Ady*Ady)+0.01,0.01)

Ax=Ax0+Adx*Ar/Ar[-1]
Ay=Ay0+Ady*Ar/Ar[-1]

Ac=曲線(x=Ax,z=Ay,y=AA*sin(Ak*Ar-Aw*t+Ap),顏色=顏色.cyan,半徑=0.2)
As0=球面(pos=向量([Ax0,0,Ay0]),半徑=0.1,顏色=顏色.cyan)
As1=球面(pos=向量([Ax1,0,Ay1]),半徑=0.1,顏色=顏色.cyan)

Alabel=標籤(pos=向量([Ax0,0,Ay0]),文字="Ar=%4.2f" % (Ar[-1]),顏色=顏色.cyan,yoffset=-60,opacity=0)

Asource=箭頭(pos=As0.位置,axis=向量(0,Ac.y[0],0),顏色=顏色.cyan)
Atarget=箭頭(pos=As1.位置,axis=向量(0,Ac.y[-1],0),顏色=顏色.cyan)



BA=1
Bk=Ak
Bw=1
Bp=0

Bx0=0; By0=0
Bx1=10;By1=0
Bdx=Bx1-Bx0
Bdy=By1-By0
Br=arange(0,sqrt(Bdx*Bdx+Bdy*Bdy)+0.01,0.01)

Bx=Bx0+Bdx*Br/Br[-1]
By=By0+Bdy*Br/Br[-1]

Bc=曲線(x=Bx,z=By,y=BA*sin(Bk*Br-Bw*t+Bp),顏色=顏色.green,半徑=0.2)
Bs0=球面(pos=向量([Bx0,0,By0]),半徑=0.1,顏色=顏色.green)
Bs1=球面(pos=向量([Bx1,0,By1]),半徑=0.1,顏色=顏色.green)

Blabel=標籤(pos=向量([Bx0,0,By0]),文字="Br=%4.2f" % (Br[-1]),顏色=顏色.green,yoffset=-100,opacity=0)

Bsource=箭頭(pos=Bs0.位置,axis=向量(0,Bc.y[0],0),顏色=顏色.green)
Btarget=箭頭(pos=Bs1.位置,axis=向量(0,Bc.y[-1],0),顏色=顏色.green)


Xtarget=箭頭(pos=Bs1.位置,axis=向量(0,Ac.y[-1]+Bc.y[-1],0),顏色=顏色.magenta)

Xlabeld=標籤(pos=Bs1.位置,text="delta_r=%4.2f" % (Br[-1]-Ar[-1]),顏色=顏色.magenta,xoffset=-30,yoffset=100,opacity=0)
Xlabell=標籤(pos=Bs1.位置,text="lambda=%4.2f" % wavelength,color=顏色.magenta,xoffset=-30,yoffset=60,opacity=0)
Xlabelr=標籤(pos=Bs1.位置,text="ratio=%4.2f" % ((Br[-1]-Ar[-1])/wavelength),顏色=顏色.magenta,xoffset=-30,yoffset=-60,opacity=0)


n=None
drag=0    

#scene.forward=vector([0.021853,-0.923144,-0.383834])
while 1:
    頻率(40)
#    print scene.center, scene.forward, scene.range
    t += 0.1
    
    Ac.y=AA*sin(Ak*Ar-Aw*t+Ap)
    Asource.座標軸=向量(0,Ac.y[0],0)
    Atarget.座標軸=向量(0,Ac.y[-1],0)
    
    Bc.y=BA*sin(Bk*Br-Bw*t+Bp)
    Bsource.座標軸=向量(0,Bc.y[0],0)
    Btarget.座標軸=向量(0,Bc.y[-1],0)

    Xtarget.座標軸=向量(0,Ac.y[-1]+Bc.y[-1],0)

    if 場景.mouse.clicked:
        m=場景.mouse.getclick()
        newPick=場景.mouse.pick

        if newPick==As0:
            print (" A")
        elif newPick==Bs0:
            print (" B")
        elif newPick==Bs1:
            print (" X")
        else:
            print (" none")
            #scene.center=(As0.pos+Bs0.pos+As1.pos+Bs1.pos)/4.
            #scene.center=scene.mouse.pos


        print (newPick)
        if m.click == "none":
            drag=0; print (drag)
            場景.mouse.getclick()
            場景.center=場景.mouse.位置
        elif m.click == "left":
            n=newPick
            drag=1; print (drag)
            
    if drag==1:
        #print "Drag ",
        #print scene.mouse.button
        if n!=None:
            n.位置[0]=場景.mouse.位置[0]
            n.位置[2]=場景.mouse.位置[2]

            newpos=n.位置
            if n==As0:
                Ax0=newpos[0]
                Ay0=newpos[2]
                As0.位置=向量([Ax0,0,Ay0])

            elif n==Bs0:
                Bx0=newpos[0]
                By0=newpos[2]
                Bs0.位置=向量([Bx0,0,By0])
            elif n==Bs1:
                Ax1=newpos[0]
                Ay1=newpos[2]
                Bx1=newpos[0]
                By1=newpos[2]
                As1.位置=向量([Ax1,0,Ay1])
                Bs1.位置=向量([Bx1,0,By1])

            else:
                print ("none")


            Adx=Ax1-Ax0
            Ady=Ay1-Ay0
            Ar=arange(0,sqrt(Adx*Adx+Ady*Ady)+0.01,0.01)
            Alabel.位置=向量([Ax0,0,Ay0])
            Alabel.文字="Ar=%4.2f" % (Ar[-1])


            Ax=Ax0+Adx*Ar/Ar[-1]
            Ay=Ay0+Ady*Ar/Ar[-1]
            Aold=Ac
            Ac=曲線(x=Ax,z=Ay,y=AA*sin(Ak*Ar-Aw*t+Ap),顏色=顏色.cyan,半徑=.2)
            Aold.可見的=0

            Asource.位置=向量([Ax0,0,Ay0])
            Atarget.位置=向量([Ax1,0,Ay1])

            Bdx=Bx1-Bx0
            Bdy=By1-By0
            Br=arange(0,sqrt(Bdx*Bdx+Bdy*Bdy)+0.01,0.01)
            Blabel.位置=向量([Bx0,0,By0])
            Blabel.文字="Br=%4.2f" % (Br[-1])

            Bx=Bx0+Bdx*Br/Br[-1]
            By=By0+Bdy*Br/Br[-1]
            Bold=Bc
            Bc=曲線(x=Bx,z=By,y=BA*sin(Bk*Br-Bw*t+Bp),顏色=顏色.green,半徑=.2)
            Bold.可見的=0

            Bsource.位置=向量([Bx0,0,By0])
            Btarget.位置=向量([Bx1,0,By1])

            Xtarget.位置=向量([Bx1,0,By1])
            Xlabeld.位置=Bs1.位置
            Xlabeld.文字="delta_r=%4.2f" % (Br[-1]-Ar[-1])
            Xlabell.位置=Bs1.位置
            Xlabell.文字="lambda=%4.2f" % wavelength
            Xlabelr.位置=Bs1.位置
            Xlabelr.文字="ratio=%4.2f" % ((Br[-1]-Ar[-1])/wavelength)


            

