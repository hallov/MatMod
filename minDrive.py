import numpy as np
import scipy.optimize as scipy
from pulp import *
import math as math
cap=150
prodPoints=3
needPoints=8

needs=np.array([1600,610,330,170,130,130,120,90]) #Data från sheets
prod=np.array([930,1500,750])
dist=np.array(
    [[47,23,14,54,46,37,28,111], #älm
      [47,1,27,55,38,28,27,98], #gbg
      [55,22,6,62,54,46,36,119]]) #helborg

model=LpProblem("Transpor",LpMinimize) #Startar problemt
x=LpVariable.dicts("X",((i,j) for j in range(needPoints) for i in range(prodPoints)),0,None)
#X är 3x8 matris
def funx(x): #vad vi ska minimisera
    sum=0
    for i in range (3):
        for j in range(8):
            sum+=2*dist[i,j] *x[i,j]/cap
    return sum

model+= funx(x),"TransCost"
def sumRow(x,nbr):  #summera x i en rad dvs de som fabrik skickar ut
    sum=0
    for i in range (8):
        sum+=x[nbr,i]
    return sum
model+=sumRow(x,0)<=np.ceil(prod[0]), "Prod 1" #lägger till krav för produktion
model+=sumRow(x,1)<=np.ceil(prod[1]), "Prod 2"
model+=sumRow(x,2)<=np.ceil(prod[2]), "Prod 3"
def sumCol(x,nbr): #summera x i kolumn, dvs hur mycket alla grossister får
    sum=0
    for i in range (3):
        sum+=x[i,nbr]
    return sum
for i in range(8):  #lägger till kraven hos grossisterna
    model+=sumCol(x,i)==np.ceil(needs[i])

model.solve(GLPK_CMD()) #löser problemt
print("Status:", LpStatus[model.status]) #utdata
for v in model.variables():
    if (np.round(v.varValue/150)==0):
        print(v.name, "=", np.round(v.varValue/150))
    else:
        print(v.name, "=", np.round(v.varValue/150)," 1/",np.round(np.abs(1/((v.varValue/150)-np.round(v.varValue/150)))))
print("Stärcka ", model.objective.value(),"mil avg")