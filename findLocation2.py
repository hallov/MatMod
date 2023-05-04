import numpy as np
import itertools
from sympy import Symbol, nsolve
from sympy import*
eqn=[]
x1=Symbol('x1')
x2=Symbol('x2')
x3=Symbol('x3')
x4=Symbol('x4')
# x5=Symbol('x5')
# x6=Symbol('x6')
def addData2(px,py,alpha,teta,eqn,type): #lägger till data till ekv system 
    R=np.array([[cos(teta),sin(teta)],[-sin(teta),cos(teta)]])
    P=np.array([[1,0,-px],[0,1,-py]])
    for i in range (len(alpha)):
        v=np.array([-sin(alpha[i]),cos(alpha[i])])
        #print(type)
        
        # U=np.array([[x1],[x2],[1]])
        # tot=np.matmul(np.matmul(np.matmul(v,R),P),U)
        if ((type==0 and i==0)or(type==1 and i==1)): #avgör vilke alfa som hör ihop med vilket u ( vi testra all komb)
            U=np.array([[x1],[x2],[1]])
            eqn.append(np.matmul(np.matmul(np.matmul(v,R),P),U))
        elif ((type==0 and i==1)or(type==1 and i==0)):
            U=np.array([[x3],[x4],[1]])
            eqn.append(np.matmul(np.matmul(np.matmul(v,R),P),U))
     
    return eqn
def dataHantering(combo,eqn): #hanterar vilken data som läggs till samt testar datan
    eqn=addData2(0,0,([pi/2,pi/3]),0,eqn,combo[0])
    eqn=addData2(0.5,0,([pi/2,pi*2/3]),0,eqn,combo[1])
    #eqn=addData2(0.5,0,([pi/2,pi*2/3]),0,eqn,combo[2])
    eqn=addData2(-0.5,0,([pi/3,atan(sqrt(3)/2)]),0,eqn,combo[2])
    #print(eqn)
    try:
        sol= nsolve((eqn),(x1,x2,x3,x4),(0,0,0,0)) #checkar om systemet har lösning
        print("löst")
        print(sol)
    except (ValueError,ZeroDivisionError):
        print("saknar")
        return 
    return 

combinations = itertools.product([0, 1], repeat=3) #ger oss combos av gissnnigar
for combo in combinations:
    print(combo)
    dataHantering(combo,eqn)
    eqn=[]
 
# combinations = itertools.combinations_with_replacement([0, 1,2], 3) #ger oss combos av gissnnigar
# for combo in combinations:
#     print(combo)


# def addData(px,py,alpha,teta,constants,varibles):
#     constantTerm=np.array([px*(np.sin(alpha)*(-np.cos(teta)-np.cos(alpha)*np.sin(teta)))
#     +py*(np.cos(alpha)*np.cos(teta)-np.sin(alpha)*np.sin(teta))])
#     constants=np.vstack((constants,constantTerm))
#     varible=np.array([(np.sin(alpha)*(-np.cos(teta)-np.cos(alpha)*np.sin(teta))),(np.cos(alpha)*np.cos(teta)-np.sin(alpha)*np.sin(teta))])
#     varibles=np.vstack((varibles,varible))
#     return constants, varibles



# for i in range (2):
#     for n in range (2):
#         print(i,n)
#         dataHantering(i,n,constants,varibles)
#         constants=np.array([404])
#         varibles=np.array([404,404,404,404])

# constants=np.delete(constants,0,0)
# varibles=np.delete(varibles,0,0)
# print(constants)
# print("test")
# print(varibles)
# solution=np.linalg.solve(varibles,constants)
# print("Ux:",solution[0], "Uy:",solution[1])

#varibels=np.array([(np.sin(alpha)(-np.cos(teta)-np.cos(alpha)*np.sin(teta)))],[(np.cos(alpha)*np.cos(teta)-np.sin(alpha)*np.sin(teta))])
# v = np.array[-np.sin(alpha),np.cos(alpha)]
# p = np.array([[1,0,-px],[0,1,-py]])
# R = np.array([[np.cos(teta), np.sin(teta)],[-np.sin(teta),np.cos(teta)]])

