import numpy as np
import itertools
constants=np.array([404])
varibles=np.array([404,404,404,404])

def addData2(px,py,alpha,teta,constants,varibles,type): #lägger till data till ekv system 
    zeros=np.array([0,0])
    for i in range (len(alpha)):
        constantTerm=np.array([px*(np.sin(alpha[i])*(-np.cos(teta)-np.cos(alpha[i])*np.sin(teta))) #lägger till constanten
        +py*(np.cos(alpha[i])*np.cos(teta)-np.sin(alpha[i])*np.sin(teta))])
        constants=np.vstack((constants,constantTerm))
        varible=np.array([(np.sin(alpha[i])*(-np.cos(teta)-np.cos(alpha[i])*np.sin(teta))),(np.cos(alpha[i])*np.cos(teta)-np.sin(alpha[i])*np.sin(teta))])
        if ((type==0 and i==0)or(type==1 and i==1)): #avgör vilke alfa som hör ihop med vilket u ( vi testra all komb)
            varible=np.hstack((varible,zeros))
            varibles=np.vstack((varibles,varible))
        elif ((type==0 and i==1)or(type==1 and i==0)):
            varible=np.hstack((zeros,varible))
            varibles=np.vstack((varibles,varible))
    return constants, varibles
def dataHantering(i,n,constants,varibles): #hanterar vilken data som läggs till samt testar datan
    constants,varibles=addData2(0,0,([np.pi/2,np.pi/3]),0,constants,varibles,i)
    constants,varibles=addData2(0.5,0,([np.pi*2/3,np.pi/2]),0,constants,varibles,n)
    constants=np.delete(constants,0,0)
    varibles=np.delete(varibles,0,0)
    try:
        x1 = np.linalg.solve(varibles,constants) #checkar om systemet har lösning
        print("löst")
        print(np.round(x1,4))
    except np.linalg.LinAlgError:
        print("saknar")
        return 
    return 

combinations = itertools.combinations_with_replacement([0, 1], 2) #ger oss combos av gissnnigar
for combo in combinations:
    print(combo)
    dataHantering(*combo,constants,varibles)
    constants=np.array([404])
    varibles=np.array([404,404,404,404])
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

