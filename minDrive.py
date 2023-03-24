import numpy as np
import scipy.optimize as scipy
from pulp import *
cap=150
prodPoints=3
needPoints=8

needs=np.array([1600,610,330,170,130,130,120,90])/150 #Check sheets
prod=np.array([930,1500,750])/150
dist=np.array(
    [[47,23,14,54,46,37,28,111], #älm
      [47,1,27,55,38,28,27,98], #gbg
      [55,22,6,62,54,46,36,119]]) #helborg
distV=dist.flatten()
model=LpProblem("Transpor",LpMinimize)
x=LpVariable.dicts("X",((i,j) for j in range(needPoints) for i in range(prodPoints)),0,None,'Integer')
def funx(x):
    sum=0
    for i in range (8):
        for j in range(3):
            sum+=2*dist[j,i]*x[j,i]
    return sum
model+= funx(x),"TransCost"
def sumRow(x,nbr):
    sum=0
    for i in range (8):
        sum+=x[nbr,i]
    return sum
model+=sumRow(x,0)<=prod[0], "Prod 1"
model+=sumRow(x,1)<=prod[1], "Prod 2"
model+=sumRow(x,2)<=prod[1], "Prod 3"
def sumCol(x,nbr):
    sum=0
    for i in range (3):
        sum+=x[i,nbr]
    return sum
for i in range(8):
    model+=sumCol(x,i)==np.ceil(needs[i])
solver_list = listSolvers(onlyAvailable=True)



model.solve(GLPK_CMD())
print("Status:", LpStatus[model.status])
for v in model.variables():
    print(v.name, "=", v.varValue)
print("Stärcka ", model.objective.value(),"mil")