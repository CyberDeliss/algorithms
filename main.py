from fibonacci import fibonacci_list
from my_sort_func import bubble_sort, mix_sorting, comb_sorting, insertion_sort
from my_sort_func import selection_sort, quick_sort, merge_sort, pyramid_sort
from random import shuffle

example = fibonacci_list(20)
shuffle(example)

shuffle(example)
print(example)

bubble_sort(example)
print(example)
shuffle(example)
print(example)

mix_sorting(example)
shuffle(example)

comb_sorting(example)
shuffle(example)

insertion_sort(example)
shuffle(example)

selection_sort(example)
shuffle(example)

quick_sort(example)
shuffle(example)

merge_sort(example)
shuffle(example)

pyramid_sort(example)
shuffle(example)
