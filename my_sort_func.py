"""
1. bubble_sort O(n^2)
2. mix_sorting (shaker sorting) O(n^2)
3. comb_sorting
4. insertion_sort O(n^2) O(n^2)
5. selection_sort O(n^2)
6. quick_sort O(n^2) -> O(n)
7. merge_sort O(n log n)
8. pyramid_sort O(n log n) -> O(n)
9. tim_sort
"""


def swap_pos(lst: list, a: int, b: int) -> list:
    #using the swapping approach
    lst[a], lst[b] = lst[b], lst[a]
    return lst


def bubble_sort(_list: list) -> list:
    for i in range(0, len(_list)):
        for j in range(i, len(_list)):
            if _list[i] > _list[j]:
                _list = swap_pos(_list, i, j)
    return _list


def mix_sorting(_list: list) -> list:
    pass


def comb_sorting(_list: list) -> list:
    pass


def insertion_sort(_list: list) -> list:
    pass


def selection_sort(_list: list) -> list:
    pass


def quick_sort(_list: list) -> list:
    pass


def merge_sort(_list: list) -> list:
    pass


def pyramid_sort(_list: list) -> list:
    pass


