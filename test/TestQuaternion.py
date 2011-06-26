# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from wavemol.math import geometry

import math

class TestQuaternion(unittest.TestCase):
    def testInit(self): # fold>>
        q = geometry.Quaternion.fromVector3D( geometry.Vector3D([1.0,2.0,3.0]), math.pi/4.0 )
        
        self.assertAlmostEqual(q.w(), math.cos(math.pi/8.0))
        self.assertAlmostEqual(q.x(), 1.0*math.sin(math.pi/8.0))
        self.assertAlmostEqual(q.y(), 2.0*math.sin(math.pi/8.0))
        self.assertAlmostEqual(q.z(), 3.0*math.sin(math.pi/8.0))

    def testToRotationMatrix(self): 
        q=geometry.Quaternion.fromVector3D(geometry.Vector3D([1.0,0.0,0.0]) , 0.0615)
        m = q.toRotationMatrix()
        self.assertAlmostEqual(m[0][0], 1.0)
        self.assertAlmostEqual(m[0][1], 0.0)
        self.assertAlmostEqual(m[0][2], 0.0)
        self.assertAlmostEqual(m[1][0], 0.0)
        self.assertAlmostEqual(m[1][1], math.cos(0.0615))
        self.assertAlmostEqual(m[1][2], -math.sin(0.0615))
        self.assertAlmostEqual(m[2][0], 0.0)
        self.assertAlmostEqual(m[2][1], math.sin(0.0615))
        self.assertAlmostEqual(m[2][2], math.cos(0.0615))

        q=geometry.Quaternion.fromVector3D(geometry.Vector3D([1.0,0.0,0.0]),-0.0615)
        m = q.toRotationMatrix()
        self.assertAlmostEqual(m[0][0], 1.0)
        self.assertAlmostEqual(m[0][1], 0.0)
        self.assertAlmostEqual(m[0][2], 0.0)
        self.assertAlmostEqual(m[1][0], 0.0)
        self.assertAlmostEqual(m[1][1], math.cos(-0.0615))
        self.assertAlmostEqual(m[1][2], -math.sin(-0.0615))
        self.assertAlmostEqual(m[2][0], 0.0)
        self.assertAlmostEqual(m[2][1], math.sin(-0.0615))
        self.assertAlmostEqual(m[2][2], math.cos(-0.0615))

if __name__ == '__main__':
    unittest.main()
    
