"""This module contains tests for line.py
"""
from pprint import pprint
import sys
sys.path.append("./../..")

from pygeom import Vector3d, Point3d, Line3d

def testLine():
    point = Point3d(5.0, 1.0, 3.0)
    vector = Vector3d(1.0, 4.0, 2.0)
    line = Line3d(vector, point)
    print line

if __name__=="__main__":
    testLine()

