import numpy as np # Importera biblioteket numpy och kalla det np
import math as math
import itertools # Importera modulen itertools för att generera permutationer av en lista
from sympy import Symbol, nsolve # Importera Symbol och nsolve från sympy
from sympy import* # Importera alla andra moduler från sympy
import matplotlib.pyplot as plt

# Skapa en lista av koordinater för fyra punkter
pos=[[0,1,-2], #x
     [2,0,-1]] #y

# Skapa en lista av vinklar
angles=[pi*3/2,atan(1/2)+pi/2,0]

# Skapa tre symboler för okända variabler
px=Symbol('px') 
py=Symbol('py')
theta=Symbol('theta')

# Skapa en funktion test som testar om ett ekvationsystem har en lösning
def test(combo,pos,angles):
    eqn=[] # Skapa en tom lista för ekvationer
    for i in range (len(combo)): # Loopa genom permutationen och skapa en ekvation för varje punkt
        P=np.array([[1,0,-px],[0,1,-py]]) 
        R=np.array([[cos(theta),sin(theta)],[-sin(theta),cos(theta)]]) 
        v=np.array([-sin(angles[combo[i]]),cos(angles[combo[i]])])
        U=np.array([[pos[0][i]],[pos[1][i]],[1]]) 
        eqn.append(np.matmul(np.matmul(np.matmul(v,R),P),U)) # Lägg till ekvationen för den aktuella punkten i listan med ekvationer
    try:
        sol= nsolve((eqn),(px,py,theta),(1,-3,-0.1)) # Försök att lösa systemet av ekvationer med nsolve från sympy
        print("löst") 
        soltheta=sol[2]%np.pi # Beräkna lösningen för theta
        print("x",round(sol[0],3), "y",round(sol[1],3),"theta",soltheta) 
        #plt.arrow(sol[0],sol[1],0.05*np.cos(soltheta),0.05*np.sin(soltheta),width=0.06,zorder=2)
        plt.arrow(round(sol[0], 3), round(sol[1], 3), 0.05 * math.cos(soltheta), 0.05 * math.sin(soltheta), width=0.06, zorder=2)
        #plt.arrow(sol[0],sol[1],cos(soltheta),sin(soltheta))
    except (ValueError,ZeroDivisionError): # Om systemet inte har en lösning
        print("saknar") 
        return 
    return 

n=3 #antal sensroer
vectors = [list(perm) for perm in itertools.permutations(range(n))] # Skapa en lista av alla möjliga permutationer av en lista med n element

for combo in vectors: # Loopa genom alla möjliga permutationer
    print(combo) 
    test(combo,pos,angles) # Testar om permutationen har en lösning
plt.plot(pos[0],pos[1],'xr',label="sensor")
plt.grid(zorder=0)
plt.arrow(10,10, 0.05, 0.05 ,width=0.06,label="truck", zorder=2)
#plt.plot('b',label="Truck")
plt.xlim(-2.2,1.3)
plt.ylim(-2.3,2.6)
plt.legend()
plt.show()
# plt.plot(pos[0],pos[1],'xr',label="Sensor")


plt.arrow(0,0,0,0.05,width=0.06,label="Truck",zorder=2)
# plt.legend()
# plt.show()