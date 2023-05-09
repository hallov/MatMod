import numpy as np
import itertools
from sympy import Symbol, nsolve
from sympy import*
import matplotlib.pyplot as plt
eqn=[]   #sätter upp eqn och variblerer
x1=Symbol('x1') 
x2=Symbol('x2')
x3=Symbol('x3')
x4=Symbol('x4')
x5=Symbol('x5')
x6=Symbol('x6')
def addData2(px,py,alpha,teta,eqn,type): #lägger till data till ekv system 
    R=np.array([[cos(teta),sin(teta)],[-sin(teta),cos(teta)]])
    P=np.array([[1,0,-px],[0,1,-py]])   #sätter upp matriser
    for i in range (len(alpha)):      #testar varje alpha  
        v=np.array([-sin(alpha[i]),cos(alpha[i])])
        if(type[i])==1:              #beronde på matris korrespenderar med  olika variblar
            U=np.array([[x1],[x2],[1]])
            eqn.append(np.matmul(np.matmul(np.matmul(v,R),P),U))
        elif(type[i])==2:
            U=np.array([[x3],[x4],[1]])
            eqn.append(np.matmul(np.matmul(np.matmul(v,R),P),U))
        elif(type[i])==3:
            U=np.array([[x5],[x6],[1]])
            eqn.append(np.matmul(np.matmul(np.matmul(v,R),P),U))
    return eqn
def dataHantering(combo,eqn): #hanterar vilken data som läggs till samt testar datan
    eqn=addData2(0,0,([pi/2,pi/3,pi*3/2]),0,eqn,combo[0])    #indata
    eqn=addData2(0.5,0,([pi/2,pi*2/3,atan(2/0.5)+pi]),0,eqn,combo[1])
    eqn=addData2(-0.5,0,([pi/3,atan(sqrt(3)/2),2*pi-atan(2/0.5)]),0,eqn,combo[2])
    try:
        sol= nsolve((eqn),(x1,x2,x3,x4,x5,x6),(1,0,0,0,0,0.1)) #checkar om systemet har lösning
        print("löst")
        print(sol)
    except (ValueError,ZeroDivisionError):
        print("saknar")
        return 
    return 
perms = list(itertools.permutations([1, 2, 3]))  #fixar alla kominationer av matriser mha magi
matrices = list(itertools.product(perms, repeat=3))
result = [m for m in matrices if all(row.count(1)==1 and row.count(2)==1 and row.count(3)==1 for row in m)] #ger oss bara möjliga
# for combo in result:   
#     print(combo)
#     dataHantering(combo,eqn)
#     eqn=[]
plt.arrow(0,0,0.01,0,width=0.06,label="Truck",zorder=2,head_length=0.1)
plt.arrow(-0.5,0,0.01,0,width=0.06,zorder=2,head_length=0.1)
plt.arrow(0.5,0,0.01,0,width=0.06,zorder=2,head_length=0.1)
plt.ylim([-1,1.006])
plt.xlim([-0.55,0.65])
plt.grid(zorder=0)
plt.legend()
plt.show()
plt.plot(0,0.866,'xr',label="Sensor")
plt.plot(0.5,0.866,'xr')
plt.plot(0,-2,'xr')
plt.arrow(0,0,0.01,0,width=0.06,label="Truck",zorder=2,head_length=0.1)
plt.arrow(-0.5,0,0.01,0,width=0.06,zorder=2,head_length=0.1)
plt.arrow(0.5,0,0.01,0,width=0.06,zorder=2,head_length=0.1)
plt.grid(zorder=0)
plt.legend()
plt.show()