from typing import List, Optional

from searching import locate_min


def bubble_sort(array: List) -> None:
    bubbled = False
    for _ in range(len(array)):
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                array[i], array[i + 1] = array[i + 1], array[i]
                bubbled = True

        if bubbled:
            bubbled = False
        else:
            break


def selection_sort(array: List) -> None:
    n = len(array)
    for i in range(n):
        j = locate_min(array[i:]) + i
        array[i], array[j] = array[j], array[i]


def merge_sort(array: List, start: Optional[int] = None, stop: Optional[int] = None) -> None:
    if start is None:
        start = 0
    if stop is None:
        stop = len(array)

    if stop - start <= 1:
        return

    length = stop - start
    half_length = length // 2
    middle = start + half_length

    merge_sort(array, start, middle)
    merge_sort(array, middle, stop)

    helper = array[start:stop]
    i = 0
    j = half_length
    for k in range(start, stop):
        if j == length or i < half_length and helper[i] <= helper[j]:
            array[k] = helper[i]
            i += 1
        else:
            array[k] = helper[j]
            j += 1
