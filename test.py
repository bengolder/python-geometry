from core import Vector3D, Point3D
# test add
v = Vector3D(0.0, 1.0, 2.0)
v1 = v + 1
v1
v1.length - v.length

v1 = Vector3D(0.0, 2.0, 1.0)
v1.length
v2 = v1 + 4
v2.length
v3 = v1 + -7
v1 + v3
v1 - v2
v1 * v3
v3[0]
v1['x']
v1[:2]
v3[-1]
v2
v3
v4 = v3.cross(v2)
# v3 and v2 point in the same direction
v4
# this is a vector of length 0
# so it's length can't be adjusted
v4.length = 1.0

v2 = Vector3D(-4.0, 1.2, 3.5)
v1 = Vector3D(2.0, 1.1, 0.0)
v2 - v1
v2 * 1.25
v2 * v1 #dot product

p1 = Point3D(-2.2, -0.5, 0.0034)
p2 = Point3D(3.45, 0.01, -2004.665)
p1.distanceTo(p2)
p1.distanceTo(p2)
p2.vectorTo(p1)
p1 - p2

