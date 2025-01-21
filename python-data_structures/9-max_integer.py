#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Trouve le plus grand entier d'une liste.

    Args:
        my_list (list): La liste d'entiers.

    Returns:
        int: Le plus grand entier de la liste, ou None si la liste est vide.
    """
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
