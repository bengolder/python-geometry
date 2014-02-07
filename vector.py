import math
import numbers
from core import isRoughlyZero

class VectorBase(object):
    """Should not be instantiated directly
    """
    @property
    def length(self):
        """get the vector length / amplitude
            >>> v = Vector3d(0.0, 2.0, 1.0)
            >>> v.length
            2.2360679774997898
        """
        # only calculate the length if asked to.
        return math.sqrt(sum(n**2 for n in self))
    @length.setter
    def length(self, number):
        """Set the vector length
        """
        return self.toLength( number )

    def normalized(self):
        """just returns the normalized version of self without editing self in
        place.
            >>> v.normalized()
            Vector3d(0.0, 0.894427191, 0.4472135955)
            >>> v
            Vector3d(0.0, 3.2995419076, 1.6497709538)
        """
        # think how important float accuracy is here!
        if isRoughlyZero(sum(n**2 for n in self)):
            raise ZeroDivisionError
        else:
            return self * (1 / self.length)

    def toLength(self, number):
        """Get a parallel vector with the input amplitude."""
        # depends on normalized() and __mul__
        # create a vector as long as the number
        return self.normalized() * number

    def __iter__(self):
        """For iterating, the vectors coordinates are represented as a tuple."""
        return self.coords.__iter__()

    def dot(self, other):
        """Gets the dot product of this vector and another.
            >>> v
            Vector3d(5, 1.20747670785, 60.0)
            >>> v1
            Vector3d(0.0, 2.0, 1.0)
            >>> v1.dot(v)
            62.41495341569977
        """
        return sum((p[0] * p[1]) for p in zip(self, other))

    def __add__(self, other):
        """we want to add single numbers as a way of changing the length of the
        vector, while it would be nice to be able to do vector addition with
        other vectors.
            >>> from core import Vector3d
            >>> # test add
            ... v = Vector3d(0.0, 1.0, 2.0)
            >>> v1 = v + 1
            >>> v1
            Vector3d(0.0, 1.4472135955, 2.894427191)
            >>> v1.length - v.length
            0.99999999999999956
            >>> v1 + v
            Vector3d(0.0, 2.4472135955, 4.894427191)
        """
        if isinstance(other, numbers.Number):
            # then add to the length of the vector
            # multiply the number by the normalized self, and then
            # add the multiplied vector to self
            return self.normalized() * other + self

    def __sub__(self, other):
        """Subtract a vector or number
            >>> v2 = Vector3d(-4.0, 1.2, 3.5)
            >>> v1 = Vector3d(2.0, 1.1, 0.0)
            >>> v2 - v1
            Vector3d(-6.0, 0.1, 3.5)
        """
        return self.__add__(other * -1)

    def __mul__(self, other):
        """if with a number, then scalar multiplication of the vector,
            if with a Vector, then dot product, I guess for now, because
            the asterisk looks more like a dot than an X.
            >>> v2 = Vector3d(-4.0, 1.2, 3.5)
            >>> v1 = Vector3d(2.0, 1.1, 0.0)
            >>> v2 * 1.25
            Vector3d(-5.0, 1.5, 4.375)
            >>> v2 * v1 #dot product
            -6.6799999999999997
        """
        if isinstance(other, numbers.Number):
            # scalar multiplication for numbers
            return self.__class__( *((n * other) for n in self))

        elif isinstance(other, self.__class__):
            # dot product for other vectors
            return self.__class__(other)

    def __hash__(self):
        """This method provides a hashing value that is the same hashing value
        returned by the vector's coordinate tuple. This allows for testing for
        equality between vectors and tuples, as well as between vectors.

        Two vector instances (a and b) with the same coordinates would return True
        when compared for equality: a == b, a behavior that I would love to
        have, and which would seem very intuitive.

        They would also return true when compared for equality with a tuple
        equivalent to their coordinates. My hope is that this will greatly aid
        in filtering duplicate points where necessary - something I presume
        many geometry algorithms will need to look out for.

        I'm not sure it is a bad idea, but I intend this class to basically be a
        tuple of floats wrapped with additional functionality.
        """
        return self.coords.__hash__()

    def __eq__(self, other):
        """I am allowing these to compared to tuples, and to say that yes, they
        are equal. the idea here is that a Vector3d _is_ a tuple of floats, but
        with some extra methods.
        """
        return self.coords.__eq__(other)

    def angleTo(self, other):
        """computes the angle between two vectors
            cos theta = (n * m) / (n.length * m.length)
        """
        cosTheta = (self * other) / (self.length * other.length)
        return math.acos(cosTheta)


