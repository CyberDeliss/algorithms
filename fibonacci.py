"""
the Fibonacci sequence, in which each number is the sum of
the two preceding ones. The sequence commonly starts from 0 and 1,
although some authors start the sequence from 1 and 1 or sometimes
(as did Fibonacci) from 1 and 2. Starting from 0 and 1,
the first few values in the sequence are:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
"""


def fibonacci_list(count: int) -> list:
    first = 0
    second = 1
    result = [first, second]

    for _ in range(0, count - 2):
        num = result[-1] + result[-2]
        result.append(num)
    return result


def fibonacci(count: int) -> int:
    first = 0
    second = 1
    result = [first, second]

    for _ in range(0, count - 2):
        num = result[-1] + result[-2]
        result.append(num)
        result = result[1:]
    return result


def fibonacci_recursive(count: int) -> int:
    """
    it starts from 1. For example "3" is number four
    :param count: index number of sequence
    :return: one int number from Fibonacci sequence
    """
    if count == 0:
        return 0
    if count == 1:
        return 1
    return fibonacci_recursive(count - 1) + fibonacci_recursive(count - 2)


print(f"{fibonacci(15)}\n")
print(f"{fibonacci_recursive(4)}\n")
print(f"{fibonacci_list(15)}\n")
