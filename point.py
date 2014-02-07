
class PointBase(object):
    """Should not be instantiated ditectly.
    """
    def vectorTo(self, other):
        """Find the vector to another point.
        """
        return other - self

