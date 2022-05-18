import numpy as np


points = np.array([])

#Introducem punctele din spatiu

print("Add the points: ")
for i in range(0, 4):
    pointx = float(input("x" + str(i) + " >> "))
    pointy = float(input("y" + str(i) + " >> "))
    pointz = float(input("z" + str(i) + " >> "))

    points = np.append(points, [pointx, pointy, pointz])
points = points.reshape(4, 3)

print("Add the number δ: ")
δ = float(input("δ = "))

print("Add versorul V: ")
pointx = float(input("x >> "))
pointy = float(input("y >> "))
pointz = float(input("z >> "))
V = np.array([pointx, pointy, pointz])

print("Add the pair (u,v): ")
u = float(input("u = "))
v = float(input("v = "))


a = points[1][0] + δ * V[0]
b = points[1][1] + δ * V[1]
c = points[1][2] + δ * V[2]

a1 = points[2][0] + δ * V[0]
b1 = points[2][1] + δ * V[1]
c1 = points[2][2] + δ * V[2]



points = np.append(points, points[0] + δ * V)

b11 = [a, b, c]
points = np.append(points, b11)

b21 = [a1, b1, c1]
points = np.append(points, b21)

points = np.append(points, points[3] + δ * V)

points = points.reshape(8, 3)

pointsStep1 = np.array([])
#First step
pointsStep1 = np.append(pointsStep1, (1 - u) * points[0] + u * points[1])
pointsStep1 = np.append(pointsStep1, (1 - u) * points[1] + u * points[2])
pointsStep1 = np.append(pointsStep1 , (1 - u) * points[2] + u * points[3])

pointsStep1 = pointsStep1.reshape(3,3)


pointsStep2 = np.array([])
#Second step
pointsStep2 = np.append(pointsStep2, (1 - u) * pointsStep1[0] + u * pointsStep1[1])
pointsStep2 = np.append(pointsStep2, (1 - u) * pointsStep1[1] + u * pointsStep1[2])

pointsStep2 = pointsStep2.reshape(2,3)


#Third step
b3000 = (1 - u) * pointsStep2[0] + u * pointsStep2[1]


#Second part
pointsStep1_2 = np.array([])
#Step 1
pointsStep1_2 = np.append(pointsStep1_2, (1 - u) * points[4] + u * points[5])
pointsStep1_2 = np.append(pointsStep1_2, (1 - u) * points[5] + u * points[6])
pointsStep1_2 = np.append(pointsStep1_2, (1 - u) * points[6] + u * points[7])

pointsStep1_2 = pointsStep1_2.reshape(3,3)


pointsStep2_2 = np.array([])
#Step 2
pointsStep2_2  = np.append(pointsStep2_2 , (1 - u) * pointsStep1[0] + u * pointsStep1[1])
pointsStep2_2  = np.append(pointsStep2_2 , (1 - u) * pointsStep1[1] + u * pointsStep1[2])

pointsStep2_2  = pointsStep2_2.reshape(2,3)


#Step 3
b3001 = (1 - u) * pointsStep2_2[0] + u * pointsStep2_2[1]

b3100 = (1 - v) * b3000 + v * b3001

print("r ( " + str(u) + ", " + str(v) + " ) = ( " + str(format(b3100[0], '.3f')) + ", " + str(format(b3100[1], '.3f')) + ", " + str(format(b3100[2], '.3f')) + " )/")

