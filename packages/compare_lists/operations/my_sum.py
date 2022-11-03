from numbers import Number

def my_sum(v):
    """Sums the elements of a list"""
    if not isinstance(v, list):
        raise TypeError("I only know how to sum lists.")
    sum_so_far = 0
    for elem in v:
        if not isinstance(elem, Number):
            raise TypeError("I only know how to sum numbers.")
        if isinstance(elem, complex):
            raise Exception("Let's keep it real.")
        sum_so_far += elem
    return sum_so_far