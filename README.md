# python-geometry

---

This is a project to create a decent geometry library for python.

It is more focused on abstraction and a nice api than on performance. Maybe
I'll deal with performance later.

This has barely begun

Here's some examples of what I'm trying to do:

---

## Vector3D

### Adding vectors or adding to their length

using `+` or `-`

```python
>>> v
Vector3D(-0.734099439586, 0.220229831876, 0.642337009638)
>>> v1
Vector3D(2.0, 1.1, 0.0)
>>> v1 + 2.2
Vector3D(3.92767499909, 2.1602212495, 0.0)
>>> v1.length
2.2825424421026654
>>> v1 + 2.2
Vector3D(3.92767499909, 2.1602212495, 0.0)
>>> (v1 + 2.2).length
4.4825424421026661
>>> v1 + v
Vector3D(1.26590056041, 1.32022983188, 0.642337009638)
>>> v1 - 2.2
Vector3D(0.0723250009114, 0.0397787505013, 0.0)
>>> v1 - v
Vector3D(2.73409943959, 0.879770168124, -0.642337009638)
```

### multiplication

using `*` with a number or vector. With antoher vector this returns the dot
product.

```python
>>> v2 = Vector3D(-4.0, 1.2, 3.5)
>>> v1 = Vector3D(2.0, 1.1, 0.0)
>>> v2 - v1
Vector3D(-6.0, 0.1, 3.5)
>>> v2 * 1.25
Vector3D(-5.0, 1.5, 4.375)
>>> v2 * v1 #dot product
-6.6799999999999997
```

### Vector length get and set

`.length`, and `.length = value`

```python
>>> v = Vector3D(0.0, 2.0, 1.0)
>>> v.length
2.2360679774997898
```

### Normalize vectors

`.normalized()` returns a unit vector copy of the vector, while `.normalize()`
edits the vector in place and _then_ returns a copy.

```python
>>> v
Vector3D(-4.0, 1.2, 3.5)
>>> v.normalized()
Vector3D(-0.734099439586, 0.220229831876, 0.642337009638)
>>> v
Vector3D(-4.0, 1.2, 3.5)
>>> v.normalize()
Vector3D(-0.734099439586, 0.220229831876, 0.642337009638)
>>> v
Vector3D(-0.734099439586, 0.220229831876, 0.642337009638)
```

### rebuild vector from dictionaries, iterables, or other vectors.

```python
>>> v
Vector3D(0.0, 3.2995419076, 1.6497709538)
>>> v.match({'x':2.0, 'y':1.0, 'z':2.2})
>>> v
Vector3D(2.0, 1.0, 2.2)
```

### dictionary and tuple-like behavior

```python
>>> v
Vector3D(2.0, 1.0, 2.2)
>>> v[0]
2.0
>>> v[-1]
2.2000000000000002
>>> v[:2]
(2.0, 1.0)
>>> v['y']
1.0
>>> v
Vector3D(0.0, 1.20747670785, 2.4149534157)
>>> v[0] = 5
>>> v
Vector3D(5, 1.20747670785, 2.4149534157)
>>> v['z'] = 60.0
>>> v
Vector3D(5, 1.20747670785, 60.0)
```

### dot and cross products

```python
>>> v
Vector3D(5, 1.20747670785, 60.0)
>>> v1
Vector3D(0.0, 2.0, 1.0)
>>> v1.dot(v)
62.41495341569977
>>> v
Vector3D(5, 1.20747670785, 60.0)
>>> v1
Vector3D(0.0, 2.0, 1.0)
>>> v1.cross(v)
Vector3D(118.792523292, 5.0, -10.0)
```



---

## Point3D

This is basically just a vector with other methods. You can use it as a
Vector3D.

### find the distance to another point

```python
>>> p1 = Point3D(-2.2, -0.5, 0.0034)
>>> p2 = Point3D(3.45, 0.01, -2004.665)
>>> p1.distanceTo(p2)
2004.676426897508
```

### get the vector to another point

```python
>>> p1 = Point3D(-2.2, -0.5, 0.0034)
>>> p2 = Point3D(3.45, 0.01, -2004.665)
>>> p1.distanceTo(p2)
2004.676426897508
>>> p1.distanceTo(p2)
2004.676426897508
>>> p2.vectorTo(p1)
Vector3D(-5.65, -0.51, 2004.6684)
>>> p1 - p2
Vector3D(-5.65, -0.51, 2004.6684)
```


