import math 
import numpy

import _Gohlke_transformations

class BoundVector3D(object):
    def __init__(self, start, end):
        if isinstance(start, Point3D):
            self._start = Point3D(start.coordinates())
        else:
            self._start = Point3D(start)
        
        if isinstance(end, Point3D):
            self._end = Point3D(end.coordinates())
        else:
            self._end = Point3D(end)
    def start(self):
        return self._start
    def end(self):
         return self._end

class Vector3D(object):
    """Defines a free vector"""
    @classmethod
    def fromBoundVector3D(cls, bound_vector):
        return cls(bound_vector.end().coordinates() - bound_vector.start().coordinates())
    def __init__(self, components):
        self._components=numpy.array(components)

    def components(self):
        return self._components

    def x(self):
        return self._components[0]

    def y(self):
        return self._components[1]

    def z(self):
        return self._components[2]

    def __getitem__(self, key):
        return self._components[key]

class Point3D(object):
    """Defines a point in 3D space"""
    def __init__(self, coordinates):
        self._coordinates=numpy.array(coordinates)

    def coordinates(self):
        return self._coordinates

    def x(self):
        return self._coordinates[0]

    def y(self):
        return self._coordinates[1]

    def z(self):
        return self._coordinates[2]

    def __getitem__(self, key):
        return self._coordinates[key]


class Line3D(object):
    @classmethod
    def throughPoints(cls,p1, p2):
        return cls(BoundVector3D(p1, p2))
    @classmethod
    def fromBoundVector3D(cls, vector):
        return cls(vector)
    def __init__(self,bv):
        self._bound_vector = bv
    def value(self,t):
         return Point3D( self._bound_vector.end().coordinates() * t + self._bound_vector.start().coordinates() * (1.0-t))

class Quaternion(object):
    @classmethod
    def fromVector3D(cls, axis, angle):
        w = math.cos(angle/2.0)
        s = math.sin(angle/2.0)
        x = float(axis[0])*s
        y = float(axis[1])*s
        z = float(axis[2])*s
        return cls(axis=axis, angle=angle, components=[x,y,z,w])
         
    def __init__(self, **args): 
        self._angle = args.get("angle", None)
        self._axis = args.get("axis", None)
        self._components = args.get("components", None)

    def x(self): 
        return self._components[0]
    def y(self): 
        return self._components[1]
    def z(self): 
        return self._components[2]
    def w(self): 
        return self._components[3]
    def axis(self):
        return self._axis
    def angle(self):
        return self._angle
    def __getitem__(self, key):
        return self._components[key]
    def toRotationMatrix(self): 
        return _Gohlke_transformations.quaternion_matrix(self._components)
       

xAxis3D = Vector3D( (1.0, 0.0, 0.0) )
yAxis3D = Vector3D( (0.0, 1.0, 0.0) )
zAxis3D = Vector3D( (0.0, 0.0, 1.0) )
origin3D = Point3D( (0.0, 0.0, 0.0) )
