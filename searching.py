from typing import List


def locate_min(array: List) -> int:
    if not array:
        raise ValueError('Empty array.')

    location = 0
    for i, element in enumerate(array):
        if element < array[location]:
            location = i

    return location
