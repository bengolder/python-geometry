"""
"""

import numbers
import sys

PY3 = sys.version_info[0] == 3

if PY3:
    string_type = str
else:
    string_type = basestring

# For float comparison:
def isRoughlyZero(number):
    return round(number, 7) == 0
# though there are better ways to do this.
# It would be nice if this could handle all sorts of numbers
# see:
# http://floating-point-gui.de/errors/comparison/
# http://stackoverflow.com/questions/9528421/value-for-epsilon-in-python
# http://stackoverflow.com/questions/4028889/floating-point-equality-in-python
# http://stackoverflow.com/questions/3049101/floating-point-equality-in-python-and-in-general


