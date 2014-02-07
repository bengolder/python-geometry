from vector3d import Vector3d
from point import PointBase

class Point3d(Vector3d, PointBase):
    """Functionally similar to a Vector3d, but concpetually distinct, and
    includes several additional methods.
    """
    def __init__(self, *args, **kwargs):
        Vector3d.__init__()
        PointBase.__init__()

    def __repr__(self):
        return 'Point3d(%s, %s, %s)' % self.coords

    def distanceTo(self, other):
        """Find the distance between this point and another.
        """
        if isinstance(other, Plane3d):
            # get distance between point and plane
            pass
        elif isinstance(other, Line3d):
            # get distance between point and line
            pass
        else:
            return (other - self).length


