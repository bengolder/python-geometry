import unittest2 as unittest

class TestImport(unittest.TestCase):
    def setUp(self):
        pass

    def test_imports(self):
        from geometry import (
                Interval,
                Scale,
                Box2d,
                Box3d,
                Vector2d,
                Vector3d,
                Point2d,
                Point3d,
                PointSet,
                PageX,
                PageY,
                WorldX,
                WorldY,
                WorldZ,
                Matrix,
                Line3d,
                LineSegment2d,
                Plane3d,
        )


