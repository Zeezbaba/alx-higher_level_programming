#!/usr/bin/python3
"""function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - A peak value from the list.
    """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2
        mid_next = mid + 1

        if list_of_integers[mid] < list_of_integers[mid_next]:
            low = mid_next
        else:
            high = mid

    return list_of_integers[low]
