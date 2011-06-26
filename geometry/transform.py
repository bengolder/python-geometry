from .. import geometry
import math
import numpy 

def normalize(entity): 
    """Returns a new entity, normalized to euclidean norm == 1"""
    if isinstance(entity, geometry.Vector3D):
        arr = entity.components()
        return geometry.Vector3D( (arr / math.sqrt(numpy.dot(arr, arr))))
    elif isinstance(vector,geometry.BoundVector3D):
        arr_start = vector.start().coordinates()
        arr_end = vector.end().coordinates()
        arr_end-arr_start

def rotate(entity, axis, angle):
    q = geometry.Quaternion.fromVector3D(axis, angle)
    m = numpy.array(q.toRotationMatrix())
    arr = numpy.array([ entity[0], entity[1], entity[2], 1.0 ])
    rotated = numpy.dot(m, arr)
    if type(entity) == geometry.Vector3D:
        return geometry.Vector3D( rotated )
    elif type(entity) == geometry.Point3D:
        return geometry.Point3D( rotated )

    raise TypeError("Unrecognized type") 

