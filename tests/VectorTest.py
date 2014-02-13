"""This module contains tests for vector.py
"""
import sys
sys.path.append("./../..")

from geometry import Vector3d, Point3d


def testVector():
    vA = Vector3d(1,1,1)
    print vA
    vB = Vector3d(1, -2, 3)
    print vB
    print vA * vB
    print vB * vA
    print vA.length * vB.length
    print vA.angleTo(vB)
    print vB.angleTo(vA)

if __name__=="__main__":
    testVector()
