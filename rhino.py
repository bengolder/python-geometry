"""This module handles object conversions to and from Rhino"""

import Rhino.Geometry as rg

from vector import Vector3d, Point3d, PointSet
from plane import Plane3d
from line import Line3d

def importFromRhino(objs):
    """This function detects the type of an incoming Rhino
    object and converts it into the appropriate type

    the only argument can be either a single object or a
    list or tuple of objects
    """
    if type(objs) in (list, tuple):
        for obj in objs:
            yield convertFromRhino(obj)
    else:
        return convertFromRhino(obj)

def convertFromRhino(obj):
    return importAndConvert[type(obj)](obj)

def exportToRhino(objs):
    """This function detects the type of outgoing objects and
    converts them to the appropriate type of Rhinoo object
    """
    if type(objs) in (list, tuple):
        for obj in objs:
            yield exportToRhino(obj)
    else:
        return exportToRhino(obj)

def exportToRhino(obj):
    return convertAndExport[type(obj)](obj)


importAndConvert = {
        rg.Vector3d: lambda g: Vector3d(g.X, g.Y, g.Z),
        rg.Point3d: lambda g: Point3d(g.X, g.Y, g.Z),
        rg.Point: lambda g: importFromRhino(g.Location),
        rg.Plane: lambda g: Plane3d(
            importFromRhino(g.Origin),
            importFromRhino(g.Normal)),
        rg.Line: lambda g: Line3d(
            importFromRhino(g.Direction),
            importFromRhino(g.From)),
        }

convertAndExport = {
        Vector3d: lambda g: rg.Vector3d(*g),
        Point3d: lambda g: rg.Point3d(*g),
        Plane3d: lambda g: rg.Plane(
            exportToRhino(g.point),
            exportToRhino(g.normal)),
        Line3d: lambda g: rg.Line(
            exportToRhino(g.point),
            exportToRhino(g.vector)),
        }

