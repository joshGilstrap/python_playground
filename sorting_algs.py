from timeit import repeat
from random import randint
from datetime import timedelta

ARR_SIZE = 20
MAX_VALUE = 99

def time_algorithm(alg, arr):
    setup = f'from __main__ import {alg}' \
        if alg != 'sorted' else ''
    stmt = f'{alg}({arr})'
    number = 10
    times = repeat(setup=setup, stmt=stmt, repeat=3, number=number)
    print(f'Algorithm: {alg}. Best of {number} iterations: {timedelta(seconds=min(times))}')


def make_arr():
    arr = [randint(0,MAX_VALUE) for i in range(ARR_SIZE)]
    return arr


def bubble_sort(nums):
    for i, e in enumerate(nums):
        for j, f in enumerate(nums):
            if e < f:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def insertion_sort(nums):
    for i in range(1,len(nums)):
        target = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > target:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = target
    return nums


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    middle = len(nums) // 2

    left = merge_sort(nums[:middle])
    right = merge_sort(nums[middle:])
    return merge(left, right)


def merge(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    merged_arr = []
    place1 = 0
    place2 = 0
    while len(merged_arr) < (len(arr1) + len(arr2)):
        if arr1[place1] <= arr2[place2]:
            merged_arr.append(arr1[place1])
            place1 += 1
        else:
            merged_arr.append(arr2[place2])
            place2 += 1

        if place1 == len(arr1):
            merged_arr += arr2[place2:]
            break
        if place2 == len(arr2):
            merged_arr += arr1[place1:]
            break
    return merged_arr


def quick_sort(nums):
    if len(nums) < 2:
        return nums

    pivot = nums[randint(0,len(nums) - 1)]

    lower, middle, higher = [], [], []
    for i, e in enumerate(nums):
        if e < pivot:
            lower.append(nums[i])
        elif e > pivot:
            higher.append(nums[i])
        else:
            middle.append(nums[i])
    return quick_sort(lower) + middle + quick_sort(higher)

def run_sort():
    n = make_arr()
    print(f'\nArray Size: {len(n)}')
    print(f'Value range: (0, {MAX_VALUE})')
    print('|-----------------------------------------------------------------------------|\n')
    time_algorithm('bubble_sort', n)
    print('\n')
    time_algorithm('insertion_sort', n)
    print('\n')
    time_algorithm('merge_sort', n)
    print('\n')
    time_algorithm('quick_sort', n)
    print('\n')
    print('|-----------------------------------------------------------------------------|\n')
