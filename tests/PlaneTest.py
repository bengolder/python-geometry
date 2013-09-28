"""This module contains tests for plane.py
"""
import sys
sys.path.append("./../..")

from pygeom import Vector3d, Point3d, Line3d, Plane3d



def testPlane():
    point = Point3d(5.0, 1.0, 3.0)
    vector = Vector3d(1.0, 4.0, 2.0)
    planeA = Plane3d(point, vector)
    print planeA

    P = Point3d(1.0, 3.0, 2.0)
    Q = Point3d(3.0, -1.0, 6.0)
    R = Point3d(5.0, 2.0, 0)
    planeB = Plane3d(P, Q, R)
    print planeB

    print planeB.angleTo(planeA)


if __name__=="__main__":
    testPlane()



