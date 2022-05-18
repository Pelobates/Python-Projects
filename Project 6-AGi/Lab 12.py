import numpy as np

puncte = np.array([])

print("introduceti gradul suprafetei: ")
g = int(input("g = ")) #gradul suprafetei

print("introduceti punctele: ")
for i in range(0, int((g+1)*(g+2)/2)):
    punctx = float(input("x" + str(i) + " >> "))
    puncty = float(input("y" + str(i) + " >> "))
    punctz = float(input("z" + str(i) + " >> "))

    puncte= np.append(puncte, [punctx, puncty, punctz])

puncte = puncte.reshape(int((g+1)*(g+2)/2), 3)

print("introduceti tripletul: ")
u0 = float(input("u0 = "))
v0 = float(input("v0 = "))
w0 = float(input("w0 = "))


def calcul_pozitie(n):
    p = []
    val = 0
    for i in range(0, n):
        val = val + 2
        p.append(val)
        for j in range(1, i + 1):
            val = val + 1
            p.append(val)
    return p


def aplica_Casteljeau(n, puncte, u0, v0, w0):
    PuncteNoi = np.array([])

    p1 = calcul_pozitie(n) #pozitie punctelor din stanga
    p2 = []                       #pozitie punctelor din dreapta
    for i in range(len(p1)):
        p2.append(p1[i] - 1)
    for i in range(0, int((n+1)*(n+2)/2) - n - 1):
        PuncteNoi = np.append(PuncteNoi, u0 * puncte[p1[i]] + v0 * puncte[i] + w0 * puncte[p2[i]])

    PuncteNoi = PuncteNoi.reshape(int(PuncteNoi.__len__()/3), 3)
    return PuncteNoi

PuncteNoi = puncte
for i in range(g, 0, -1):
    new__points = aplica_Casteljeau(i, PuncteNoi, u0, v0, w0)

print('\n')
print("r(u, v, w) = (" + str(PuncteNoi[0][0]) + ', ' + str(PuncteNoi[0][1]) + ', ' + str(PuncteNoi[0][2]) + ' )')

