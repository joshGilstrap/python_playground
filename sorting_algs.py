import timeit
import random

ARR_SIZE = 100

def make_arr():
    arr = []
    for num in range(ARR_SIZE):
        num = random.randint(0,999)
        arr.append(num)
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

n = make_arr()
print(n)
insertion_sort(n)
print(n)
