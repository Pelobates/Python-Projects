import numpy as np
import math
import matplotlib.pyplot as plt
import turtle
import string

#a = np.ones((3,3))        # a 2D array with 3 rows, 2 columns, filled with ones"
#b = np.array([1,2,3])     # a 1D array initialised using a list [1,2,3]
#c = np.linspace(2,3,100)  # an array with 100 points beteen (and including) 2 and 3

a = (0, 1, 0)
b = (1, 0, 1)
c = (0, -1, 2)
d = (-1, 0, 3)

A = np.array([a, b, c, d])
I = np.eye(3)


def translationMatrix(dx=0, dy=0, dz=0):
    """ Return matrix for translation along vector (dx, dy, dz). """

    return np.array([[1, 0, 0, 0],
                     [0, 1, 0, 0],
                     [0, 0, 1, 0],
                     [dx, dy, dz, 1]])



print(translationMatrix(2, 3, 4))

color_lut = 'rgbc'
fig = plt.figure()
ax = plt.gca()
xs = []
ys = []
for row in A:
    output_row = I @ row
    x, y, i = output_row
    xs.append(x)
    ys.append(y)
    i = int(i) # convert float to int for indexing
    c = color_lut[i]
    plt.scatter(x, y, color=c)
    plt.text(x + 0.15, y, f"{string.ascii_letters[i]}")
xs.append(xs[0])
ys.append(ys[0])
plt.plot(xs, ys, color="gray", linestyle='dotted')
ax.set_xticks(np.arange(-2.5, 3, 0.5))
ax.set_yticks(np.arange(-2.5, 3, 0.5))
plt.grid()
plt.show()


T_s = np.array([[2, 0, 0], [0, 2, 0], [0, 0, 1]])

fig = plt.figure()
ax = plt.gca()
xs_s = []
ys_s = []
for row in A:
    output_row = T_s @ row
    x, y, i = row
    x_s, y_s, i_s = output_row
    xs_s.append(x_s)
    ys_s.append(y_s)
    i, i_s = int(i), int(i_s) # convert float to int for indexing
    c, c_s = color_lut[i], color_lut[i_s] # these are the same but, its good to be explicit
    plt.scatter(x, y, color=c)
    plt.scatter(x_s, y_s, color=c_s)
    plt.text(x + 0.15, y, f"{string.ascii_letters[int(i)]}")
    plt.text(x_s + 0.15, y_s, f"{string.ascii_letters[int(i_s)]}'")

xs_s.append(xs_s[0])
ys_s.append(ys_s[0])
plt.plot(xs, ys, color="gray", linestyle='dotted')
plt.plot(xs_s, ys_s, color="gray", linestyle='dotted')
ax.set_xticks(np.arange(-2.5, 3, 0.5))
ax.set_yticks(np.arange(-2.5, 3, 0.5))
plt.grid()
plt.show()





# ex 1
a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
if a != 0:
   d = b * b - 4 * a * c
   if d > 0:
    x1 = (- b + math.sqrt(d)) / 2 * a
    x2 = ( b - math.sqrt(d)) / 2 * a
    print(" radacinile sunt ", x1, x2)
   else:
    if d == 0:
      x1 = - b / 2 * a
      x2 = x1
      print("radacinile sunt egale", x1)
    else:
      print("nu avem solutii reale")
else:
  if b != 0:
    x = - c / b
    print("x este", x)
  else:
    print("nu exista x")





# ex 8


# creating turtle pen
t = turtle.Turtle()

# taking input for the no of the sides of the polygon
n = int(input("Enter the no of the sides of the polygon : "))

# taking input for the length of the sides of the polygon
l = int(input("Enter the length of the sides of the polygon : "))


for _ in range(n):
    turtle.forward(l)
    turtle.right(360 / n)






