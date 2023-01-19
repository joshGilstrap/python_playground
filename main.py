from datetime import timedelta
from timeit import repeat
from random import randint
import sorting_algs as srt

def searching_time_external(alg, arr, target):
    setup = f'from search_algs import {alg}'
    if alg == 'binary_search':
        stmt = f'{alg} ({arr}, 0, {len(arr) - 1}, {target})'
    else:
        stmt = f'{alg}({arr}, {target})'
    number = 10
    times = repeat(setup=setup, stmt=stmt, repeat=3, number=number)
    print(f'Alogrithm: {alg}. Best of {number} iterations: {timedelta(seconds=min(times))}')


def sorting_time_external(alg, arr):
    setup = f'from sorting_algs import {alg}' \
        if alg != 'sorted' else ''
    stmt = f'{alg}({arr})'
    number = 10
    times = repeat(setup=setup, stmt=stmt, repeat=3, number=number)
    print(f'Algorithm: {alg}. Best of {number} iterations: {timedelta(seconds=min(times))}')


def run_all():
    print('Running all algorithms...')
    print('\nSorting algs:')
    n = srt.quick_sort(srt.make_arr())
    tar = n[randint(0, srt.ARR_SIZE - 1)]

    print(f'Array Size: {len(n)}')
    print(f'Value range: (0, {srt.MAX_VALUE})')
    print('|-----------------------------------------------------------------------------|\n')
    sorting_time_external('bubble_sort', n)
    print('\n')
    sorting_time_external('insertion_sort', n)
    print('\n')
    sorting_time_external('merge_sort', n)
    print('\n')
    sorting_time_external('quick_sort', n)
    print('\n')
    print('|-----------------------------------------------------------------------------|\n')

    print('Searching algs:')
    print(f'Array Size: {len(n)}')
    print(f'Value range: (0, {srt.MAX_VALUE})')
    print(f'Target: {tar}')
    print('|-----------------------------------------------------------------------------|\n')
    searching_time_external('linear_search', n, tar)
    print('\n')
    searching_time_external('binary_search', n, tar)
    print('\n')
    print('|-----------------------------------------------------------------------------|\n')

run_all()
