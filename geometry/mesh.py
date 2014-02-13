import math
import numbers

from .core import isRoughlyZero
from .vector3d import Vector3d
from .point3d import Point3d
from .points import PointSet

class Edge(object):
    """This is a class roughly equivalent to a line segment. It is basically a
        connection between two points. It should behave like a tuple of two
        points.
    """
    def __init__(self, start, end):
        """The initialization methods assumes that it will receive two points
        """
        self.points = (start, end)

    def __getitem__(self, key):
        return self.points.__getitem__(key)

    def __len__(self):
        return self[0].distanceTo(self[1])

class PlanarFace(object):
    """This is meant to hold triangles and polygon facets for mesh-lik
    structures.
    """
    pass

class Edge(object):
    """An object that links two points"""
    def __init__(start, end):
        self.points = (start, end)
        self.start = self.points[0]
        self.end = self.points[1]

    @property
    def length(self):
        """Get the length of this Edge (the distance between two points)
        """
        return self.end.distanceTo(self.start)

class Polyline(PointSet):
    """An object that contains a point set and links between the points."""
    pass


class Polygon(PointSet):
    """An object that basically contains a point set and links between points
    that result in a closed shape, but has methods for using it
    in polygon-related activities.
    """
    pass

class MeshVertex(Point3D):
    """A point3d for use within a mesh that has all the functionality of a
    point, but also contains adjacency information.
    """
    def __init__(self):
        self.adjacentEdges = []

class MeshFace(object):
    """A mesh face has a set of edges that are all connected into a closed
    polygon.
    """
    def __init__(self):
        self.edges = []

class MeshEdge(Edge):
    """An edge with adjacency information.
    """
    def __init__(self):
        self.adjacentFaces = []
        self.adjacentEdges = []


class WingedEdgeMesh(object):
    """A mesh that stores adjacency information between faces, edges and
    vertices.
    """
    def __init__(self):
        self.faces = []
        self.edges = []
        self.vertices = []
        pass



