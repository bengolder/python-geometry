import unittest
import random
import math

from geometry import Vector2d, Vector3d, Point2d, Point3d

class CoordGenerator:
    def __init__(self, scale=100, dim=3, number_type=float):
        self.bounds = (
                scale / -2,
                scale / 2
                )
        self.dim = dim
        self.number_type = number_type

    def __call__(self):
        if self.number_type == int:
            coords = [random.randint(*self.bounds) for i in range(self.dim)]
        else:
            coords = [random.uniform(*self.bounds) for i in range(self.dim)]
        return coords

    def point(self):
        if self.dim == 3:
            return Point3d(*self())
        else:
            return Point2d(*self())


class TestVectors(unittest.TestCase):

    def setUp(self):
        self.gen = CoordGenerator()
        self.coords = [self.gen() for i in range(10)]
        self.d2 = {'x':45, 'y':-453}
        self.d3 = {'x':543, 'y':-9872183, 'z':-32.543}
        self.vectors2d = [Vector2d(c[:2]) for c in self.coords]
        self.vectors3d = [Vector3d(c) for c in self.coords]
        self.v2 = Vector2d(**self.d2)
        self.v3 = Vector3d(**self.d3)

    def test_vector_members(self):
        self.assertEqual( self.v2.y, -453 )
        self.assertEqual( self.v2[0], 45 )
        # should not have been converted to a float
        self.assertNotEqual( type(self.v3['x']), type(543.0) )
        v = Vector2d( 3, 4 )
        self.assertEqual( v.length, 5 )
        w = v.toLength( 10 )
        self.assertAlmostEqual( w.x, 6 )
        coords = (6, 8, 10)
        for i, c in enumerate(w):
            self.assertAlmostEqual(c, coords[i])
        m = v.toLength(0.0)
        call_normal = lambda x: x.normalized()
        self.assertRaises(ZeroDivisionError, call_normal, m)


    def test_vector_operators(self):
        # test +, *, -
        v = Vector2d( -6, -8)
        u = Vector2d( 3, 4)
        w = v + u
        self.assertAlmostEqual(w.length, 5)
        w = v - u
        self.assertAlmostEqual(w.length, 15)
        w = v + 10
        self.assertAlmostEqual(w.length, 20)
        self.assertAlmostEqual(v * u, -50)
        self.assertEqual(v * u, u * v)
        w = u * 2
        self.assertAlmostEqual(w.length, 10)
        coords = [c for c in u]
        w = Vector2d( *coords )
        self.assertTrue( w.coords == u.coords )
        self.assertTrue( w == u )
        self.assertFalse( w is u )
        self.assertAlmostEqual(v.angleTo(u), math.pi)
        add = lambda n: w + n
        mul = lambda n: w * n
        self.assertRaises(TypeError, add, 'string')
        self.assertRaises(TypeError, mul, 'string')
        d = {w:10}
        self.assertEqual(d[u], 10)


class TestPoints(TestVectors):

    def test_point_constructor(self):
        pass

    def test_point_operators(self):
        pass

