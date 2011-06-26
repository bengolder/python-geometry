# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from wavemol.math import geometry 

class TestBoundVector3D(unittest.TestCase):
    def testInit(self):
        v = geometry.BoundVector3D( (0.0, 0.0, 0.0), (1.0,2.0,3.0) )
       
        self.assertEqual(v.start().__class__, geometry.Point3D)
        self.assertEqual(v.start()[0], 0.0)
        self.assertEqual(v.start()[1], 0.0)
        self.assertEqual(v.start()[2], 0.0)

        self.assertEqual(v.end().__class__, geometry.Point3D)
        self.assertEqual(v.end()[0], 1.0)
        self.assertEqual(v.end()[1], 2.0)
        self.assertEqual(v.end()[2], 3.0)


if __name__ == '__main__':
    unittest.main()
    
