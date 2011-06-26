# @author Stefano Borini
import os; import sys; script_path=sys.path[0]; sys.path.append(os.path.join(script_path, "../../../"));
import unittest

from wavemol.math import geometry 

class TestLine3D(unittest.TestCase):
    def testInit(self):
        l = geometry.Line3D.throughPoints( geometry.Point3D( ( 0.0, 0.0, 0.0) ), geometry.Point3D( (1.0,2.0,3.0) ) )

        self.assertEqual(l.value(1.0).__class__, geometry.Point3D)
        self.assertEqual(l.value(1.0)[0], 1.0)
        self.assertEqual(l.value(1.0)[1], 2.0)
        self.assertEqual(l.value(1.0)[2], 3.0)
        
        self.assertEqual(l.value(0.5)[0], 0.5)
        self.assertEqual(l.value(0.5)[1], 1.0)
        self.assertEqual(l.value(0.5)[2], 1.5)

if __name__ == '__main__':
    unittest.main()
    
