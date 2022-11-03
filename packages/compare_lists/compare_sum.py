from .operations.my_sum import my_sum

def compare_sum(v,w):
    if my_sum(v) == my_sum(w):
        return True
    else:
        return False