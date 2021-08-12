from typing import List

from pytest import fixture

from sorting import bubble_sort, selection_sort, merge_sort, quick_sort


@fixture
def numbers():
    return [65, -36, -19, 72, 40, -76, -78, -79, 7, 26, -16, -6, -26, -88, -81, -12, 52, -88, -50,
            -19, 74, -29, -66, -72, -68, -48, -73, 71, -37, -54, -22, 70, -83, -71, 92, 51, 79, -15,
            82, -35, -8, 82, 77, -71, -94, 84, -27, -44, 66, -56, 7, 57, -31, -91, -84, -2, -14, 95,
            83, 52, 48, 83, 57, 92, -74, -100, -99, 16, 28, 99, -42, -19, -9, -7, 0, -43, -40, 12,
            -62, -6, 91, -93, 10, -15, 8, -95, -95, 5, 48, -70, 0, 88, -17, 19, -6, -23, 43, -79,
            18, -36]


def is_ascending(array: List) -> bool:
    return all(array[i] <= array[i + 1] for i in range(len(array) - 1))


def test_bubble_sort(numbers):
    bubble_sort(numbers)
    assert is_ascending(numbers)


def test_selection_sort(numbers):
    selection_sort(numbers)
    assert is_ascending(numbers)


def test_merge_sort(numbers):
    merge_sort(numbers)
    assert is_ascending(numbers)


def test_quick_sort(numbers):
    quick_sort(numbers)
    assert is_ascending(numbers)
