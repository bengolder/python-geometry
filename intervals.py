class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.length = end - start

    def fraction(self, value):
        """given a value between the interval start and end,
        this returns a fraction between 0 and 1of the distance along the interval,
        """
        return ( value - self.start ) / self.length

    def contains( self, value):
        return self.start < value < self.end

    def __call__( self, value):
        """given a percentage value along the interval, this
        returns the actual value"""
        return (self.length * value) + self.start


class Scale(object):
    def __init__(self, domain, range ):
        self.domain = Interval(*domain)
        self.range = Interval(*range)

    def __call__(self, value ):
        """converts a value in the domain to a proportional
        value in the range"""
        return self.range( self.domain.fraction( value ) )

    def reverse(self, value ):
        """converts a value in the range to a proportional
        value in the domain"""
        return self.domain( self.range.fraction( value ) )




