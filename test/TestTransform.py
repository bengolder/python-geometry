# @author Stefano Borini
import unittest
import numpy
import math

from wavemol.math import geometry 
from wavemol.math.geometry import transform
from wavemol.math.geometry import measure

class TestTransform(unittest.TestCase): 
    def testNormalize(self): 
        p1 = transform.normalize(geometry.Vector3D( (1.0,2.0,3.0) ))
        self.assertEqual(measure.norm(p1), 1.0)
    def testRotate(self):
        v = geometry.Vector3D( (2.0,0.0,0.0) )
        axis = geometry.Vector3D( (1.0,0.0,0.0) )
        rotated = transform.rotate(v, axis, math.pi/4.0)

        self.assertAlmostEqual(rotated.x(), 2.0)
        self.assertAlmostEqual(rotated.y(), 0.0)
        self.assertAlmostEqual(rotated.z(), 0.0)

        v = geometry.Vector3D( (0.0,2.0,0.0) )
       
        rotated = transform.rotate(v, axis, math.pi/4.0)

        self.assertAlmostEqual(rotated.x(), 0.0)
        self.assertAlmostEqual(rotated.y(), 2.0/math.sqrt(2.0))
        self.assertAlmostEqual(rotated.z(), 2.0/math.sqrt(2.0))

        rotated = transform.rotate(v, axis, -math.pi/4.0)

        self.assertAlmostEqual(rotated.x(), 0.0)
        self.assertAlmostEqual(rotated.y(), 2.0/math.sqrt(2.0))
        self.assertAlmostEqual(rotated.z(), -2.0/math.sqrt(2.0))

