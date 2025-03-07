from vpython import *
cofre=box(pos=vector(0,0,0),size=vector(4,3.2,2),color=color.magenta)
cabina=cylinder(pos=vector(2,1,0),size=vector(8,5,4.5),color=color.blue)
base=box(pos=vector(6,-1.5,0),size=vector(8,.2,3),color=color.green)
escape=box(pos=vector(1,2,0.5),size=vector(0.5,1,0.5),color=color.green)
llan1=cylinder(pos=vector(2,2,2),axis=vector(2,2,2),color=color.cyan)
'''
llan2
llan3
llan3
'''

velocidad = 0.5
angulo=180
llan
while True:
    rate (30)
    cabina.rotate(angle=0.05,axis=vector(1,0,0))