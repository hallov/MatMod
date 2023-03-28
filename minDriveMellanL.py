import numpy as np
import scipy.optimize as scipy
from pulp import *
import math as math
cap=150
prodPoints=4
needPoints=9
trainfactor=10

needs=np.array([1600,610,330,170,130,130,120,90]) #Data från sheets
prod=np.array([930,1500,750])
dist=np.array(
    [[47,23,14,54,46,37,28,111,46], #älm
     [47,1 ,27,55,38,28,27,98,38/trainfactor], #gbg
     [55,22,6 ,62,54,46,36,119,54], #hbg
     [11,38,60,8 ,1 ,10,19,61,1000000]]) #Väst

model=LpProblem("Transpor",LpMinimize) #Startar problemt
x=LpVariable.dicts("X",((i,j) for j in range(needPoints) for i in range(prodPoints)),0,None)
#X är 4x8 matris
def funx(x): #vad vi ska minimisera
    sum=0
    for i in range (prodPoints):
        for j in range(needPoints):
            sum+=2*dist[i,j] *x[i,j]/cap
    return sum

model+= funx(x),"TransCost"
def sumRow(x,nbr):  #summera x i en rad dvs de som fabrik skickar ut
    sum=0
    for i in range (needPoints):
        sum+=x[nbr,i]
    return sum
model+=sumRow(x,0)<=(prod[0]), "Prod 1" #lägger till krav för produktion
model+=sumRow(x,1)<=(prod[1]), "Prod 2"
model+=sumRow(x,2)<=(prod[2]), "Prod 3"

def sumCol(x,nbr): #summera x i kolumn, dvs hur mycket alla grossister får
    sum=0
    for i in range (prodPoints):
        sum+=x[i,nbr]
    return sum
model+=sumRow(x,3)<=x[1,8], "vast"
for i in range(8):  #lägger till kraven hos grossisterna
    model+=sumCol(x,i)==needs[i]

model.solve(GLPK_CMD()) #löser problemt
print("Status:", LpStatus[model.status]) #utdata
for v in model.variables():
    print(v.name, "=", np.round(v.varValue)/cap)
#     if ((v.varValue/cap)-np.round(v.varValue/cap)==0):
#         print(v.name, "=", np.round(v.varValue)/cap)
#     else:
#         print(v.name, "=", np.round(v.varValue/cap)," 1/",np.round(np.abs(1/((v.varValue/cap)-np.round(v.varValue/cap)))))
print("Stärcka ", model.objective.value(),"mil avg")