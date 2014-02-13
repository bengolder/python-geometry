
class PointBase(object):
    """Should not be instantiated directly.
    """
    def vectorTo(self, other):
        """Find the vector to another point.
        """
        return other - self

