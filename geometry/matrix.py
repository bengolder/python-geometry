"""This module contains classes for matrices in pure python (no numpy).
    Matrices are represented as lists of lists

    Relevant reading:
        * matrix api of numpy - http://stackoverflow.com/questions/3127404/how-to-represent-matrices-in-python
        * matrices can just be vectors of vectors in python - http://www.math.okstate.edu/~ullrich/PyPlug/
        * array module in python - http://docs.python.org/2/library/array.html
"""

import math
import numbers
import itertools

from .core import isRoughlyZero

class MatrixError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

class Matrix(object):
    """A class for all kinds of matrix objects.
        Matrices are immutable.
    """
    def __init__(self, table=None, rows=3, columns=3):
        """Nested iterables of values can be passed, or you can designate a size
        of the matrix. The default is 3x3 identity matrix."""
        if table:
            # just use the given table, iterate through it and convert it to
            # tuples
            self.table = tuple( [ tuple( r ) for r in table ] )
            if not self.is_rectangular():
                msg = """The iterable used to produce this Matrix had unclear
                dimensions. Either the rows or the columns (or both) are not even
                lenghts. All the rows must be the same length as each other and
                all the columns must be the same length as each other."""
                raise MatrixError( msg )
        else:
            # build an identity matrix
            self.table = []
            for i in range(rows):
                row = []
                for j in range(columns):
                    if i == j:
                        val = 1.0
                    else:
                        val = 0.0
                    row.append( val )
                self.table.append( tuple(row) )
            self.table = tuple(self.table)

    def __iter__(self):
        """iterate through the table of the matrix"""
        return self.table.__iter__()

    def full_iter(self):
        """iterate through without regard for columns or rows. This basically
        treats the Matrix as one big row."""
        for row in self:
            for item in row:
                yield item

    def __getitem__(self, key):
        """gets the row from the table of the Matrix"""
        return self.table[key]

    def __len__(self):
        """gets the number of rows in the matrix"""
        return len(self.table)

    def is_rectangular(self):
        """This method is used to ensure that all rows are the smae length and
        all columns are the same length."""
        rows = self.rows()
        for col in self.iter_cols():
            if len(col) != rows:
                return False
        cols = self.cols()
        for row in self:
            if len(row) != cols:
                return False
        return True

    def is_square(self):
        """check if this matrix has the same width and length"""
        return len(self) == self.cols()

    def cols(self):
        """return the number of columns in this matrix"""
        return len( self.table[0] )

    def rows(self):
        """return the number of rows in this matrix"""
        return len( self.table )

    def transpose(self):
        """Return a new Matrix with columns and rows transposed"""
        return Matrix( tuple(zip( *self.table ) ) )

    def iter_cols(self):
        """iterate through a transposed version of this Matrix"""
        return itertools.izip( *self.table )

    def row_map(self, function, *args):
        """map a function to each row of this matrix, and return the resulting
        matrix. This can input the corresponding rows from any number of
        matrices.
        """
        return Matrix( map(function, self, *args) )

    def cell_map(self, function, *args):
        """map a function to each cell of this matrix, and return the resulting
        matrix. additional iterables can be passed, but the function take one
        argument for each iterable. this can be used to iterate through two
        Matrices simultaneously, creating a new Matrix with the same dimension
        and new values calculated from each pair of cells from the two
        matrices.
        """
        row_map = lambda *r: map(function, *r)
        return Matrix( itertools.imap( row_map, self, *args ) )

    def __mul__( self, other ):
        """get matrix product, be sure that sizes fit.
        If multiplied with another matrix, this produces a matrix product.
        if multiplied by anything else, the other is assumed to be a number.
        """
        if isinstance( other, Matrix ):
            # matrix product
            cols = self.cols()
            rows = other.rows()
            # check if it will work
            if cols != rows:
                msg = """To find the product of two matrices, the number of
                columns in this matrix must match the number of rows in the
                other matrix. This matrix has %s columns and the other matrix
                has %s rows.""" % (cols, rows)
                raise MatrixError( msg )
            # get the product
            new = []
            # for each row in this
            for i in range(len(self)):
                newrow = []
                # for each column in other
                for j in range(other.cols()):
                    subvals = []
                    # for each value in this row (or in that column)
                    for n in range(cols):
                        # multiply this value by that value
                        subval = self[i][n] * other[n][j]
                        subvals.append(subval)
                    # sum the new values
                    value = sum(subvals)
                    newrow.append(value)
                new.append( newrow )
            # return a new Matrix object
            return Matrix( new )
        else:
            # assume it's a number
            mult = lambda x: x * other
            return self.cell_map( mult )

    def __add__( self, other ):
        """add this matrix to another, or add a number
        """
        if isinstance(other, Matrix):
            add = lambda x, y: x + y
            return self.cell_map(add, other)
        else:
            # assume it's a number
            add = lambda x: x + other
            return self.cell_map( add )

    def __sub__(self, other):
        """subtract another Matrix from this one, or subtract a number.
        """
        if isinstance(other, Matrix):
            sub = lambda x, y: x - y
            return self.cell_map(sub, other)
        else:
            # assume it's a number
            sub = lambda x: x - other
            return self.cell_map( sub )

    def __repr__(self):
        row_repr = lambda r: ', '.join([str(c) for c in r])
        return '<Matrix([\n%s\n])>' % '\n'.join(
            ['(%s)' % row_repr(r) for r in self]
            )


