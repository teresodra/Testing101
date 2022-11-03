

def my_concat(list1, list2):
    if not isinstance(list1, list) or not isinstance(list2, list):
        raise Exception("I only concatenate lists")