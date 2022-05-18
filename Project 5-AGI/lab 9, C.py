import geomdl

# Se considera cubica B-spline cu vectorul de noduri

# t = 0.5, 0.8, 1.4, 2.1, 2.4, 2.9, 4.0, 4.5, 4.9

# punctele de control sunt: d1(−2,−3), d2(−1,2), d3(2,2), d4(3,0), d5(1,−3).

from geomdl import BSpline

from geomdl import multi


from geomdl.visualization import VisMPL

# Cream curba

crv1 = BSpline.Curve()

crv2 = BSpline.Curve()

# Gradul

crv1.degree = 3

crv2.degree = 2

# Punctele de control

crv1.ctrlpts = [[-2,-3],[-1,2],[2,2],[3,0],[1,-3]]

crv2.ctrlpts = [[1.875, 9.375], [6, 0], [1.578, -3.157], [-2.857, -4.285]]

# Vectorul

crv1.knotvector = [0.5, 0.8, 1.4, 2.1, 2.4, 2.9, 4.0, 4.5, 4.9]

crv2.knotvector = [0.8, 1.4, 2.1, 2.4, 2.9, 4.0, 4.5]

c=multi.CurveContainer([crv1,crv2])

# Componenta vizuala

c.vis = VisMPL.VisCurve2D()




# Plot the curve

c.render()