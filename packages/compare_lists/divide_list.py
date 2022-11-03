
def divide_list_by_other_length(list1, list2):
    """Divides a list by the length of other list"""
    if len(list2) == 0:
        raise ZeroDivisionError
    return list1/len(list2)

def divide_list_by_its_length(list1):
    return divide_list_by_other_length(list1, list1)