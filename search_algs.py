from timeit import repeat
from random import randint
from datetime import timedelta
import sorting_algs as sa

def searching_time_internal(alg, arr, target):
    setup = f'from __main__ import {alg}'
    if alg == 'binary_search':
        stmt = f'{alg} ({arr}, 0, {len(arr) - 1}, {target})'
    else:
        stmt = f'{alg}({arr}, {target})'
    number = 10
    times = repeat(setup=setup, stmt=stmt, repeat=3, number=number)
    print(f'Alogrithm: {alg}. Best of {number} iterations: {timedelta(seconds=min(times))}')


def linear_search(nums, target):
    for i, e in enumerate(nums):
        if e == target:
            return i
    return None


def binary_search(nums, left, right, target):
    index = 0
    if left > right:
        index = None
    else:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            index = middle
        elif target > nums[middle]:
            index = binary_search(nums, middle + 1, right, target)
        else:
            index = binary_search(nums, left, middle - 1, target)
    return index


def run_search():
    n = sa.quick_sort(sa.make_arr())
    tar = n[randint(0, sa.ARR_SIZE - 1)]
    print(f'\nArray Size: {len(n)}')
    print(f'Data Range: (0, {sa.MAX_VALUE})')
    print(f'Target: {tar}')
    print('|-----------------------------------------------------------------------------|\n')
    searching_time_internal('linear_search', n, tar)
    print('\n')
    searching_time_internal('binary_search', n, tar)
    print('\n')
    print('|-----------------------------------------------------------------------------|\n')
