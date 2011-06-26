import numpy
import math

from . import _Gohlke_transformations
from . import transform

from .. import geometry

def angle(*args):
    """Returns the angle in radians among entities. 
    It accepts the following arguments
    - three points p1, p2, and p3: computes the angle formed by p1\p2/p3. """
    if len(args) == 3:
        p1, p2, p3 = args

    first = transform.normalize(geometry.Vector3D.fromBoundVector3D(geometry.BoundVector3D(p2, p1)))
    second = transform.normalize(geometry.Vector3D.fromBoundVector3D(geometry.BoundVector3D(p2, p3)))

    return math.atan2( 
                    norm( geometry.Vector3D(numpy.cross(second.components(), first.components()))),
                    numpy.dot(second.components(), first.components())
                ) 

def distance(entity_1, entity_2):
    if isinstance(entity_1, geometry.Point3D) and isinstance(entity_2, geometry.Point3D):
        return _Gohlke_transformations.norm(entity_2.coordinates()-entity_1.coordinates())
    else:
        raise TypeError("Unrecognized types")

def norm(entity):
    """Returns the euclidean norm of a vector"""
    if isinstance(entity, geometry.Vector3D):
        components = entity.components()
    elif isinstance(entity, geometry.BoundVector3D):
        components = entity.end().coordinates() - entity.start().coordinates()
    else:
        raise TypeError("Unrecognized entity type")

    return _Gohlke_transformations.norm(components)
        
         
    
