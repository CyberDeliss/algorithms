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
    steps = 0
    for i in range(0, len(_list)):
        for j in range(i, len(_list)):
            steps += 1
            if _list[i] > _list[j]:
                _list = swap_pos(_list, i, j)
    print(f"{steps} steps in bubble_sort")
    return _list


def mix_sorting(my_list: list) -> list:
    """
    it is bidirectional: the algorithm does not move strictly from left to right,
    but first from left to right, then from right to left.
    :param my_list:
    :return: sorted list
    """
    steps: int = 0
    left: int = 0
    right: int = len(my_list) - 1

    while right >= left:
        for i in range(right, left, -1):
            steps += 1
            if my_list[i] < my_list[i - 1]:
                steps += 1
                my_list = swap_pos(my_list, i-1, i)
        left += 1

        for i in range(left, right):
            steps += 1
            if my_list[i + 1] < my_list[i]:
                my_list = swap_pos(my_list, i, i+1)
        right -= 1

    print(f"{steps} steps in mix_sorting")
    return my_list


def comb_sorting(my_list: list) -> list:
    """
    The initial interval should not be chosen randomly,
    but taking into account a special value - the reduction factor,
    the optimal value of which is 1.247. Initially,
    the spacing between elements will be equal to the len of the list divided by 1.247;
    at each subsequent step, the distance will again be divided by
    the reduction factor - and so on until the end of the algorithm.

    :param my_list:
    :return: sorted list
    """
    steps: int = 0


    print(f"{steps} steps in comb_sorting")
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


