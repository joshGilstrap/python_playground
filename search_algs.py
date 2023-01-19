from random import randint
import sorting_algs as sa

# def binary_search(nums):
#     target = nums[randint(0, sa.ARR_SIZE - 1)]
#     print(target, '\n')
#     # check = len(nums) // 2
#     # for i in nums:
#     #     if nums[check] == nums[target]:
#     #         return check
#     #     if nums[check] > nums[target]:
#     #         check = nums[check:]
#     #         break
#     #     check = nums[:check]
#     #     break
#     # return None
#     while len(nums) > 1:
#         check = len(nums) // 2
#         if nums[check] == target:
#             return check
#         if nums[check] > target:
#             nums = nums[:check]
#         elif nums[check] < target:
#             nums = nums[check:]
#     return None


def binary_search(nums, left, right, target):
    if left > right:
        return None
    check = (right - left) // 2
    while nums[check] != target:
        if target > nums[check]:
            left = check
            binary_search(nums, left, right, target)
        elif target < nums[check]:
            right = check
            binary_search(nums, left, right, target)
    return check


n = sa.quick_sort(sa.make_arr())
print(n)
tar = n[randint(0, sa.ARR_SIZE - 1)]
print(tar)
print(binary_search(n, 0, len(n) - 1, tar))
