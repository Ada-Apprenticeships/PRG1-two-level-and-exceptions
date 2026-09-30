"""
Optional stretch. Deciding that a program should stop.

Sometimes catching an error is wrong, and the right thing is to
raise one yourself so that a caller has to deal with it.
"""


def average(readings):
    """The average of a list of readings."""
    if len(readings) == 0:
        raise ValueError("Cannot average an empty list of readings")
    return sum(readings) / len(readings)


def average_or_zero(readings):
    """The same thing, with the awkward case swallowed."""
    if len(readings) == 0:
        return 0
    return sum(readings) / len(readings)


print(average([82, 141, 47]))
print(average_or_zero([]))

try:
    print(average([]))
except ValueError as problem:
    print(f"Caught: {problem}")
