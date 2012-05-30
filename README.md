# python-geometry

---

This is a project to create a decent geometry library for python.

It is more focused on abstraction and a nice api than on performance. Maybe
I'll deal with performance later.

This has barely begun

Here's some examples of what I'm trying to do:

---

## Vectors

### Increase vectors by a length

```python
    >>> from core import Vector3D
    >>> v1 = Vector3D(0.0, 2.0, 0.0)
    >>> v1.length
    2.0
    >>> # now I'll add to the vector's amplitude
    >>> v2 = v1 + 4
    >>> v2
    Vector3D(0.0, 6.0, 0.0)
    >>> v2.length
    6.0
```

### Scalar multiplication

```python
    >>> from core import Vector3D
    >>> v1 = Vector3D(0.0, 2.0, 0.0)
    >>> v2 = v1 * 0.5
    >>> v2
    Vector3D(0.0, 1.0, 0.0)
```

### Vector length get and set

```python
    >>> v = Vector3D(0.0, 2.0, 1.0)
    >>> v.length
    2.2360679774997898
```

### Normalize vectors




