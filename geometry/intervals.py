import numbers
import math

class Interval(object):
    """
        Intervals are one-dimensional spaces on a number line

        They can be instantiated with:
            no arguments - which defaults to an interval of 0.0 to 1.0
            a single number argument - which becomes an interval from 0.0 to
                that number
            a single iterable - the interval derives the max and min of the
                iterable
            two arguments, which become the start and end of the interval
            more arguments - this derives the max and min of all the
                arguments.
        divide using an integer (into equal pieces)
        divide using a float (into pieces with a remainder)
        convert a set of numbers, instead of just one

       The interval is half-open by default. In other words, the start value is
       included in the interval, but the end value is not . [start, end)
    """
    def __init__(self, *args):
        if len(args) == 0:
            start = 0.0
            end = 1.0
        elif len(args) == 1:
            if hasattr(args[0], '__iter__'):
                start = min(args[0])
                end = max(args[0])
            elif isinstance( args[0], numbers.Number ):
                # assume we have a width
                start = 0.0
                end = start + args[0]
            else:
                start = 0.0
                end = 1.0

        elif len(args) == 2:
            # assume we have a start and end
            start = args[0]
            end = args[1]
        else: # assume we have an iterable of numbers
            # use the bounds of the numbers
            start = min(args)
            end = max(args)
        self.start = start
        self.end = end
        self.length = end - start
        self.start_open = True
        self.end_open = False

    def fraction(self, *args):
        """given a value between the interval start and end,
        this returns a fraction between 0 and 1of the distance along the interval,
        """
        if len( args ) > 1:
            return [(arg - self.start) / self.length for arg in args]
        else:
            return ( args[0] - self.start ) / self.length

    def contains( self, value):
        """tests if a value falls within the interval's bounds"""
        return self.start <= value < self.end

    def __call__( self, *args):
        """given a fractional value along the interval (between
        0.0 and 1.0), this returns the actual value"""
        if len( args ) > 1:
            return [((self.length * arg) + self.start) for arg in args]
        else:
            return (self.length * args[0]) + self.start

    def divide(self, number ):
        """
            given an integer n, divide into n equal parts
            given a float n, divide into m parts of size n, and one remainder
            returns an iterator that yeilds new Interval objects
        """
        if isinstance( number, int ):
            # divide into n parts
            step = self.length / number
            start = self.start
            end = self.start
            for i in range(number):
                steps = i + 1
                if steps < number:
                    end = steps * step
                else:
                    end = self.end
                interval = Interval( start, end )
                start = end
                yield interval
        else:
            # use this number to divide
            steps = int( math.ceil( abs(self.length / number) ) )
            start = self.start
            end = self.start
            for i in range(steps):
                this_step = i + 1
                if this_step < steps:
                    end = this_step * number
                else:
                    end = self.end
                interval = Interval( start, end )
                start = end
                yield interval

    def include(self, number):
        """Returns a new interval containing the number
            If this interval contains the number already,
            it will return a copy of this interval.
        """
        if self.contains(number):
            return Interval(self.start, self.end)
        else:
            return Interval(self.start, self.end, number)

    def scale(self, number):
        """return a new interval with start * number and end * number"""
        return Interval( self.start * number, self.end * number )

    def shift(self, number):
        """return a new interval by adding number to start and end
        """
        return Interval( self.start + number, self.end + number )

    def __repr__(self):
        start  = "[" if self.start_open else "("
        end = "]" if self.end_open else ")"
        return "Interval%s%s, %s%s" % (start, self.start, self.end, end)



class Scale(object):
    def __init__(self, domain=(0.0, 1.0), range=(0.0, 1.0) ):
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




