"""
An attempt to make a pure python, pythonic, and very abstracted geometry
library that spans from vectors to NURBS, and includes lots of useful
algorithms. I intend to value abstraction and portability over
performance where necessary. Towards that end I don't plan to use numpy or
other awesome and amazing modules that performance-oriented developers might
use.

Here's some examples:

    >>> from core import Vector3d, Point3d
    >>> # test add
    ... v = Vector3d(0.0, 1.0, 2.0)
    >>> v1 = v + 1
    >>> v1
    Vector3d(0.0, 1.4472135955, 2.894427191)
    >>> v1.length - v.length
    0.99999999999999956
    >>>
    >>> v1 = Vector3d(0.0, 2.0, 1.0)
    >>> v1.length
    2.2360679774997898
    >>> v2 = v1 + 4
    >>> v2.length
    6.2360679774997889
    >>> v3 = v1 + -7
    >>> v1 + v3
    Vector3d(0.0, -2.260990337, -1.1304951685)
    >>> v1 - v2
    Vector3d(0.0, -3.577708764, -1.788854382)
    >>> v1 * v3
    -10.652475842498529
    >>> v3[0]
    0.0
    >>> v1['x']
    0.0
    >>> v1[:2]
    (0.0, 2.0)
    >>> v3[-1]
    -2.1304951684997055
    >>> v2
    Vector3d(0.0, 5.577708764, 2.788854382)
    >>> v3
    Vector3d(0.0, -4.260990337, -2.1304951685)
    >>> v4 = v3.cross(v2)
    >>> # v3 and v2 point in the same direction
    ... v4
    Vector3d(0.0, -0.0, 0.0)
    >>> # this is a vector of length 0
    ... # so it's length can't be adjusted
    ... v4.length = 1.0
    Traceback (most recent call last):
      File "<stdin>", line 3, in <module>
      File "core.py", line 119, in length
        v = self.normalized() * number
      File "core.py", line 147, in normalized
        raise ZeroDivisionError
    ZeroDivisionError
    >>> p1 = Point3d(*v3)
    >>> p2 = Point3d(3.45, 0.01, -2004.665)
    >>> p1.distanceTo(p2)
    2002.5420312440888
    >>> p2.vectorTo(p1)
    Vector3d(-3.45, -4.270990337, 2002.53450483)
    >>> p1 - p2
    Vector3d(-3.45, -4.270990337, 2002.53450483)

First development target: intersections!!

References

[Geometry]
    http://plib.sourceforge.net/sg/index.html

[API]
    Check out the python data model emulation stuff here:
    http://docs.python.org/reference/datamodel.html

classes:

    float
    Vec2
    Vec3
    Vec4
    Mat4
    Coord
    Line3
    LineSegment3
    Quat
    Sphere
    Box
    Frustum
"""

import math
import numbers

# For float comparison:
def isRoughlyZero(number):
    return round(number, 7) == 0
# though there are better ways to do this.
# It would be nice if this could handle all sorts of numbers
# see:
# http://floating-point-gui.de/errors/comparison/
# http://stackoverflow.com/questions/9528421/value-for-epsilon-in-python
# http://stackoverflow.com/questions/4028889/floating-point-equality-in-python
# http://stackoverflow.com/questions/3049101/floating-point-equality-in-python-and-in-general


