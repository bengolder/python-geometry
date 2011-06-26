# @author Stefano Borini
import unittest
import numpy
import math

from wavemol.math import geometry 
from wavemol.math.geometry import measure

class TestMeasure(unittest.TestCase): 
    def testNormBoundVector3D(self):
        self.assertEqual( measure.norm(geometry.BoundVector3D( (0.0,0.0, 0.0), (1.0, 2.0, 3.0) )), math.sqrt(14.0))

    def testNormVector3D(self):
        self.assertEqual( measure.norm(geometry.Vector3D( (1.0, 2.0, 3.0) )), math.sqrt(14.0))

    def testDistance(self): 
        p1 = geometry.Point3D( (1.0,2.0,3.0) )
        p2 = geometry.Point3D( (2.0,2.0,3.0) )
        self.assertEqual(measure.distance(p1, p2), 1.0)

    def testAngle(self): 
        p1 = geometry.Point3D( (1.0,0.0,0.0) )
        p2 = geometry.Point3D( (0.0,0.0,0.0) )
        p3 = geometry.Point3D( (0.0,1.0,0.0) )
        self.assertEqual(measure.angle(p1, p2, p3), math.pi/2.0 )
