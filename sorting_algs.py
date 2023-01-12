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

n = make_arr()
print(n)
bubble_sort(n)
print(n)

def insertion_sort(nums):
    for i, e in enumerate(nums):
        if e > nums[i+1]:
            
            
