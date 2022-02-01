# Making a change to the first line of the code to see changes... for GitHub
#import copy
import math
import numpy as np
from numpy.linalg import inv

#import matplotlib.pyplot as plt

# Constants
E = 210 #(Kn/mm^2)
A = ((3*2*22)+(3*42))#(mm^2)
L = 163 #(mm)

# Variables
theta_MIN = (0.092155)
theta_MAX = (1.378642)





####### INPUT VARIABLES HERE ###########################
offset = 0.0 #rads 0.104876 = 6 degree offset : tan^-1(30-20)/(285-190)
theta = 0.8982 #rads 0.8982 GIVES LOAD OF 450 KN & 0.5135 Gives min loading
load = 450 #KG
#######################################################





# Functions of theta
Lift_height = (2*(163*math.sin(theta))+30) #mm
print("The calculated lift height is: ",Lift_height)

# Aim is to enter theta into a for loop returning displacement value and subsequently to plot it.

Load_Kn = load*9.81/1000
#Loading is not applied until lift_height = 190 and load increases linearly up to max lift height
if 190 < Lift_height < 285:
    load_value = np.round((Load_Kn * (((2*(163*math.sin(theta))+30)) - 190)/95),2) # Kn
else:
    load_value = 0

print("Current load applied at theta @ input: ",theta,"Radians")
print("Current load value: ",load_value,"Kn") # LOAD ACTS VERTICALLY DOWN
Q_LOAD = ([[(-load_value/2)*math.cos(theta)],[(-load_value/2)*math.sin(theta)],[(-load_value/2)*math.cos(theta)],[(-load_value/2)*math.sin(theta)],[(-load_value/2)*math.cos(theta)],[(-load_value/2)*math.sin(theta)],[(load_value/2)*math.cos(theta)],[(-load_value/2)*math.sin(theta)],[(load_value/2)*math.cos(theta)],[(-load_value/2)*math.sin(theta)],[(load_value/2)*math.cos(theta)],[(-load_value/2)*math.sin(theta)]])
print("")
print("Current offset applied: ",offset, "Radians")

print("")



# Element A (Node 1 to 2) (reactions 1,2-3,4)

angA = (3.14159265-theta+offset) #(rads)

# Top left quadrant NF 1 2-1 2
Aa11 = math.cos(angA)**2
Aa12 = math.cos(angA)*math.sin(angA)
Aa21 = math.cos(angA)*math.sin(angA)
Aa22 = math.sin(angA)**2

k11_12 = (E*A/L)*np.array([[Aa11,Aa12],[Aa21,Aa22]])


#Top right quadrant NF 3 4-1 2
Ab11 = math.cos(angA)**2
Ab12 = math.cos(angA)*math.sin(angA)
Ab21 = math.cos(angA)*math.sin(angA)
Ab22 = math.sin(angA)**2

k12_12 = (E*A/L)*np.array([[Ab11,Ab12],[Ab21,Ab22]])


#Bottom left quadrant NF 1 2-3 4
Ac11 = math.cos(angA)**2
Ac12 = math.cos(angA)*math.sin(angA)
Ac21 = math.cos(angA)*math.sin(angA)
Ac22 = math.sin(angA)**2

k21_12 = (E*A/L)*np.array([[Ac11,Ac12],[Ac21,Ac22]])


#Bottom right quadrant NF 3 4-3 4
Ad11 = math.cos(angA)**2
Ad12 = math.cos(angA)*math.sin(angA)
Ad21 = math.cos(angA)*math.sin(angA)
Ad22 = math.sin(angA)**2

k22_12 = (E*A/L)*np.array([[Ad11,Ad12],[Ad21,Ad22]])

#Concatinate along vertical axis'
top = np.concatenate((k11_12,k12_12), axis=1)
bottom = np.concatenate((k21_12,k22_12), axis=1)

#concatenate top and bottom along horrizontal axis
# k1g (global stiffness matrix for
kAg = np.concatenate((top,bottom), axis=0)

print("Stiffness matrix for element A (kA)= : ")
print(np.round(kAg,3))




#Element B (Node 2 to 3) (reactions 3,4 - 5,6)

#theta = (0.092155) #(rads)
#theta = angB

#Top left quadrant NF 3 4-3 4
Ba11 = math.cos(theta+offset)**2
Ba12 = math.cos(theta+offset)*math.sin(theta+offset)
Ba21 = math.cos(theta+offset)*math.sin(theta+offset)
Ba22 = math.sin(theta+offset)**2

k11_23 = (E*A/L)*np.array([[Ba11,Ba12],[Ba21,Ba22]])


#Top right quadrant NF 5 6-3 4
Bb11 = math.cos(theta+offset)**2
Bb12 = math.cos(theta+offset)*math.sin(theta+offset)
Bb21 = math.cos(theta+offset)*math.sin(theta+offset)
Bb22 = math.sin(theta+offset)**2

k12_23 = (E*A/L)*np.array([[Bb11,Bb12],[Bb21,Bb22]])


#Bottom left quadrant NF 3 4-5 6
Bc11 = math.cos(theta+offset)**2
Bc12 = math.cos(theta+offset)*math.sin(theta+offset)
Bc21 = math.cos(theta+offset)*math.sin(theta+offset)
Bc22 = math.sin(theta+offset)**2

k21_23 = (E*A/L)*np.array([[Bc11,Bc12],[Bc21,Bc22]])


#Bottom right quadrant NF 5 6-5 6
Bd11 = math.cos(theta+offset)**2
Bd12 = math.cos(theta+offset)*math.sin(theta+offset)
Bd21 = math.cos(theta+offset)*math.sin(theta+offset)
Bd22 = math.sin(theta+offset)**2

k22_23 = (E*A/L)*np.array([[Bd11,Bd12],[Bd21,Bd22]])

#Concatinate along vertical axis'
top = np.concatenate((k11_23,k12_23), axis=1)
bottom = np.concatenate((k21_23,k22_23), axis=1)

#concatenate top and bottom along horrizontal axis
# k1g (global stiffness matrix for
kBg = np.concatenate((top,bottom), axis=0)

print(" ")
print("Stiffness matrix for element B (kB) = : ")
print(np.round(kBg,3))

print("")



#Element C (Node 4 to 5) (reactions 7,8-9,10)

#theta = angC

#Top left quadrant NF 7 8-7 8
Ca11 = math.cos(theta+offset)**2
Ca12 = math.cos(theta+offset)*math.sin(theta+offset)
Ca21 = math.cos(theta+offset)*math.sin(theta+offset)
Ca22 = math.sin(theta+offset)**2

k11_12 = (E*A/L)*np.array([[Ca11,Ca12],[Ca21,Ca22]])


#Top right quadrant NF 9 10-7 8
Cb11 = math.cos(theta+offset)**2
Cb12 = math.cos(theta+offset)*math.sin(theta+offset)
Cb21 = math.cos(theta+offset)*math.sin(theta+offset)
Cb22 = math.sin(theta+offset)**2

k12_12 = (E*A/L)*np.array([[Cb11,Cb12],[Cb21,Cb22]])


#Bottom left quadrant NF 7 8-9 10
Cc11 = math.cos(theta+offset)**2
Cc12 = math.cos(theta+offset)*math.sin(theta+offset)
Cc21 = math.cos(theta+offset)*math.sin(theta+offset)
Cc22 = math.sin(theta+offset)**2

k21_12 = (E*A/L)*np.array([[Cc11,Cc12],[Cc21,Cc22]])


#Bottom right quadrant NF 9 10-9 10
Cd11 = math.cos(theta+offset)**2
Cd12 = math.cos(theta+offset)*math.sin(theta+offset)
Cd21 = math.cos(theta+offset)*math.sin(theta+offset)
Cd22 = math.sin(theta+offset)**2

k22_12 = (E*A/L)*np.array([[Cd11,Cd12],[Cd21,Cd22]])

#Concatinate along vertical axis'
top = np.concatenate((k11_12,k12_12), axis=1)
bottom = np.concatenate((k21_12,k22_12), axis=1)

#concatenate top and bottom along horrizontal axis
# k1g (global stiffness matrix for
kCg = np.concatenate((top,bottom), axis=0)

print("Stiffness matrix for element C (kC)= : ")
print(np.round(kCg,3))




#Element D (node 5 to 6) (reactions 9,10-11,12)

angD = angA #(rads)

#Top left quadrant NF 9 10-9 10
Da11 = math.cos(angD)**2
Da12 = math.cos(angD)*math.sin(angD)
Da21 = math.cos(angD)*math.sin(angD)
Da22 = math.sin(angD)**2

k11_23 = (E*A/L)*np.array([[Da11,Da12],[Da21,Da22]])


#Top right quadrant NF 11 12-9 10
Db11 = math.cos(angD)**2
Db12 = math.cos(angD)*math.sin(angD)
Db21 = math.cos(angD)*math.sin(angD)
Db22 = math.sin(angD)**2


k12_23 = (E*A/L)*np.array([[Db11,Db12],[Db21,Db22]])


#Bottom left quadrant NF 9 10-11 12
Dc11 = math.cos(angD)**2
Dc12 = math.cos(angD)*math.sin(angD)
Dc21 = math.cos(angD)*math.sin(angD)
Dc22 = math.sin(angD)**2

k21_23 = (E*A/L)*np.array([[Dc11,Dc12],[Dc21,Dc22]])


#Bottom right quadrant NF 11 12-11 12
Dd11 = math.cos(angD)**2
Dd12 = math.cos(angD)*math.sin(angD)
Dd21 = math.cos(angD)*math.sin(angD)
Dd22 = math.sin(angD)**2

k22_23 = (E*A/L)*np.array([[Dd11,Dd12],[Dd21,Dd22]])

#Concatinate along vertical axis'
top = np.concatenate((k11_23,k12_23), axis=1)
bottom = np.concatenate((k21_23,k22_23), axis=1)

#concatenate top and bottom along horrizontal axis
# k1g (global stiffness matrix for
kDg = np.concatenate((top,bottom), axis=0)

print(" ")
print("Stiffness matrix for element D (kD) = : ")
print(np.round(kDg,3))

print("")


#Element F (node 3 to 6) (reactions 5,6-11,12)

ThetaF = (0+offset) #(rads)
LF = 30 #mm

#Top left quadrant NF 9 10-9 10
Fa11 = math.cos(ThetaF)**2
Fa12 = math.cos(ThetaF)*math.sin(ThetaF)
Fa21 = math.cos(ThetaF)*math.sin(ThetaF)
Fa22 = math.sin(ThetaF)**2

k11_23 = (E*A/L)*np.array([[Fa11,Fa12],[Fa21,Fa22]])


#Top right quadrant NF 11 12-9 10
Fb11 = math.cos(ThetaF)**2
Fb12 = math.cos(ThetaF)*math.sin(ThetaF)
Fb21 = math.cos(ThetaF)*math.sin(ThetaF)
Fb22 = math.sin(ThetaF)**2

k12_23 = (E*A/L)*np.array([[Fb11,Fb12],[Fb21,Fb22]])


#Bottom left quadrant NF 9 10-11 12
Fc11 = math.cos(ThetaF)**2
Fc12 = math.cos(ThetaF)*math.sin(ThetaF)
Fc21 = math.cos(ThetaF)*math.sin(ThetaF)
Fc22 = math.sin(ThetaF)**2

k21_23 = (E*A/L)*np.array([[Fc11,Fc12],[Fc21,Fc22]])


#Bottom right quadrant NF 11 12-11 12
Fd11 = math.cos(ThetaF)**2
Fd12 = math.cos(ThetaF)*math.sin(ThetaF)
Fd21 = math.cos(ThetaF)*math.sin(ThetaF)
Fd22 = math.sin(ThetaF)**2

k22_23 = (E*A/LF)*np.array([[Fd11,Fd12],[Fd21,Fd22]])

#Concatinate along vertical axis'
top = np.concatenate((k11_23,k12_23), axis=1)
bottom = np.concatenate((k21_23,k22_23), axis=1)

#concatenate top and bottom along horrizontal axis
# k1g (global stiffness matrix for
kFg = np.concatenate((top,bottom), axis=0)

print(" ")
print("Stiffness matrix for element F (kF) = : ")
print(np.round(kFg,3))

print("")

#Element E (node 2 to 5) (reactions 3,4-9,10)

thetaE = ThetaF #(rads)
Le = (30+(2*163*math.cos(theta))) #(meters) the length changes with lift
Ae = (3.14159265*(5^2))
print("length of Member E = ",Le)

#Top left quadrant NF 3 4-3 4
Ea11 = math.cos(thetaE)**2
Ea12 = math.cos(thetaE)*math.sin(thetaE)
Ea21 = math.cos(thetaE)*math.sin(thetaE)
Ea22 = math.sin(thetaE)**2

k11_23 = (E*Ae/Le)*np.array([[Ea11,Ea12],[Ea21,Ea22]])


#Top right quadrant NF 9 10-3 4
Eb11 = math.cos(thetaE)**2
Eb12 = math.cos(thetaE)*math.sin(thetaE)
Eb21 = math.cos(thetaE)*math.sin(thetaE)
Eb22 = math.sin(thetaE)**2

k12_23 = (E*Ae/Le)*np.array([[Eb11,Eb12],[Eb21,Eb22]])


#Bottom left quadrant NF 3 4-9 10
Ec11 = math.cos(thetaE)**2
Ec12 = math.cos(thetaE)*math.sin(thetaE)
Ec21 = math.cos(thetaE)*math.sin(thetaE)
Ec22 = math.sin(thetaE)**2

k21_23 = (E*Ae/Le)*np.array([[Ec11,Ec12],[Ec21,Ec22]])


#Bottom right quadrant NF 9 10-9 10
Ed11 = math.cos(thetaE)**2
Ed12 = math.cos(thetaE)*math.sin(thetaE)
Ed21 = math.cos(thetaE)*math.sin(thetaE)
Ed22 = math.sin(thetaE)**2

k22_23 = (E*Ae/Le)*np.array([[Ed11,Ed12],[Ed21,Ed22]])


#Concatinate along vertical axis'
top = np.concatenate((k11_23,k12_23), axis=1)
bottom = np.concatenate((k21_23,k22_23), axis=1)

#concatenate top and bottom along horrizontal axis
# k1g (global stiffness matrix for
kEg = np.concatenate((top,bottom), axis=0)



print(" ")
print("Stiffness matrix for element E (kE) = : ")
print(np.round(kEg,3))

print("")

#Redefining values for global stiffness matrix

# kA
Aa11 = kAg[0][0]
Aa12 = kAg[0][1]
Aa21 = kAg[1][0]
Aa22 = kAg[1][1]

Ab11 = kAg[0][2]
Ab12 = kAg[0][3]
Ab21 = kAg[1][2]
Ab22 = kAg[1][3]

Ac11 = kAg[2][0]
Ac12 = kAg[2][1]
Ac21 = kAg[3][0]
Ac22 = kAg[3][1]

Ad11 = kAg[2][2]
Ad12 = kAg[2][3]
Ad21 = kAg[3][2]
Ad22 = kAg[3][3]

#kB
Ba11 = kBg[0][0]
Ba12 = kBg[0][1]
Ba21 = kBg[1][0]
Ba22 = kBg[1][1]

Bb11 = kBg[0][2]
Bb12 = kBg[0][3]
Bb21 = kBg[1][2]
Bb22 = kBg[1][3]

Bc11 = kBg[2][0]
Bc12 = kBg[2][1]
Bc21 = kBg[3][0]
Bc22 = kBg[3][1]

Bd11 = kBg[2][2]
Bd12 = kBg[2][3]
Bd21 = kBg[3][2]
Bd22 = kBg[3][3]

# kC
Ca11 = kCg[0][0]
Ca12 = kCg[0][1]
Ca21 = kCg[1][0]
Ca22 = kCg[1][1]

Cb11 = kCg[0][2]
Cb12 = kCg[0][3]
Cb21 = kCg[1][2]
Cb22 = kCg[1][3]

Cc11 = kCg[2][0]
Cc12 = kCg[2][1]
Cc21 = kCg[3][0]
Cc22 = kCg[3][1]

Cd11 = kCg[2][2]
Cd12 = kCg[2][3]
Cd21 = kCg[3][2]
Cd22 = kCg[3][3]

#kD
Da11 = kDg[0][0]
Da12 = kDg[0][1]
Da21 = kDg[1][0]
Da22 = kDg[1][1]

Db11 = kDg[0][2]
Db12 = kDg[0][3]
Db21 = kDg[1][2]
Db22 = kDg[1][3]

Dc11 = kDg[2][0]
Dc12 = kDg[2][1]
Dc21 = kDg[3][0]
Dc22 = kDg[3][1]

Dd11 = kDg[2][2]
Dd12 = kDg[2][3]
Dd21 = kDg[3][2]
Dd22 = kDg[3][3]

#kF
Fa11 = kFg[0][0]
Fa12 = kFg[0][1]
Fa21 = kFg[1][0]
Fa22 = kFg[1][1]

Fb11 = kFg[0][2]
Fb12 = kFg[0][3]
Fb21 = kFg[1][2]
Fb22 = kFg[1][3]

Fc11 = kFg[2][0]
Fc12 = kFg[2][1]
Fc21 = kFg[3][0]
Fc22 = kFg[3][1]

Fd11 = kFg[2][2]
Fd12 = kFg[2][3]
Fd21 = kFg[3][2]
Fd22 = kFg[3][3]

#kE
Ea11 = kEg[0][0]
Ea12 = kEg[0][1]
Ea21 = kEg[1][0]
Ea22 = kEg[1][1]

Eb11 = kEg[0][2]
Eb12 = kEg[0][3]
Eb21 = kEg[1][2]
Eb22 = kEg[1][3]

Ec11 = kEg[2][0]
Ec12 = kEg[2][1]
Ec21 = kEg[3][0]
Ec22 = kEg[3][1]

Ed11 = kEg[2][2]
Ed12 = kEg[2][3]
Ed21 = kEg[3][2]
Ed22 = kEg[3][3]


print("The Assembled Global Stiffness Matrix K: ")

K_m1 = np.array([[Aa11],[Aa12],[Ab11],[Ab12],[0],[0],[0],[0],[0],[0],[0],[0]])
K_m2 = np.array([[Aa21],[Aa22],[Ab21],[Ab22],[0],[0],[0],[0],[0],[0],[0],[0]])
K_m3 = np.array([[Ac11],[Ac12],[Ad11+Ba11+Ea11],[Ad12+Ba12+Ea12],[Bb11],[Bb12],[0],[0],[Eb11],[Eb12],[0],[0]])
K_m4 = np.array([[Ac21],[Ac22],[Ad21+Ba21+Ea21],[Ad22+Ba22+Ea22],[Bb21],[Bb22],[0],[0],[Eb21],[Eb22],[0],[0]])
K_m5 = np.array([[0],[0],[Ba11],[Bc12],[Bd11+Fa11],[Bd12+Fa12],[0],[0],[0],[0],[Fb11],[Fb22]])
K_m6 = np.array([[0],[0],[Bc21],[Bc22],[Bd21+Fa21],[Bd22+Fa22],[0],[0],[0],[0],[Fb21],[Fb22]])
K_m7 = np.array([[0],[0],[0],[0],[0],[0],[Ca11],[Ca12],[Cb11],[Cb12],[0],[0]])
K_m8 = np.array([[0],[0],[0],[0],[0],[0],[Ca21],[Ca22],[Cb21],[Cb22],[0],[0]])
K_m9 = np.array([[0],[0],[Ec11],[Ec12],[0],[0],[Cc11],[Cc12],[Cd11+Da11+Ed11],[Cd12+Da12+Ed12],[Db11],[Db12]])
K_m10 = np.array([[0],[0],[Ec21],[Ec22],[0],[0],[Cc21],[Cc22],[Cd21+Da21+Ed21],[Cd22+Da22+Ed22],[Db21],[Db22]])
K_m11 = np.array([[0],[0],[0],[0],[Fc11],[Fc12],[0],[0],[Dc11],[Dc12],[Dd11+Fd11],[Dd12+Fd12]])
K_m12 = np.array([[0],[0],[0],[0],[Fc21],[Fc22],[0],[0],[Dc21],[Dc22],[Dd21+Fd21],[Dd22+Fd22]])


K = np.concatenate((K_m1,K_m2,K_m3,K_m4,K_m5,K_m6,K_m7,K_m8,K_m9,K_m10,K_m11,K_m12), axis=1)
K = np.round(K,0)
K = K.astype(int) #Converts the float values to integers

print(K)

print("")
print("Q (Loading in Kn) is expressed via this (12 X 1) matrix: ")
print(Q_LOAD)
print("")

# The following code multiplies the matrices using numpy code which seemingly gives a questionably bigger value

K_inv = inv(K) #Inverts the K matrix
Delta =np.dot(K_inv,Q_LOAD) #Gets the dot product of Q * Inverse K
print("The following is the displacement matrix: ")
print(Delta)
print("" )





print("At theta (radians) =",theta,", offset =", offset,"and Lift height =",Lift_height ,"mm : the following values have been calculated: ")
deflection = (Delta[11])
deflection = np.round(deflection,2)
print("Vertical Deflection at node 6 member D: ",-deflection,"mm")

deflection2 = (Delta[9])
deflection2 = np.round(deflection2,2)
print("Vertical Deflection at node 5 member C: ", -deflection2,"mm")

deflection3 = (Delta[3])
deflection3 = np.round(deflection3,2)
print("Vertical Deflection at node 2 member A: ", -deflection3,"mm")


# Does the dot matrix command account for the determinant of the matrix? the value outputted seems too high
#determinant = np.linalg.det(K)
#print (1/determinant)

