# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from wavemol.math import geometry 

class TestVector3D(unittest.TestCase):
    def testInit(self):
        v = geometry.Vector3D( (1.0,2.0,3.0) )
       
        self.assertAlmostEqual(v.x(), 1.0)
        self.assertAlmostEqual(v.y(), 2.0)
        self.assertAlmostEqual(v.z(), 3.0)

        self.assertAlmostEqual(v[0], 1.0)
        self.assertAlmostEqual(v[1], 2.0)
        self.assertAlmostEqual(v[2], 3.0)

if __name__ == '__main__':
    unittest.main()
    
