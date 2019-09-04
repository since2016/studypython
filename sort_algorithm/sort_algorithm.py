
import math

def bubble_sort(nums):
    for i in range(1, len(nums)):
        for j in range(0, len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def merge_sort(nums):
    if(len(nums) < 2):
        return nums
    mid = math.floor(len(nums)/2)
    left, right = nums[0:mid], nums[mid:]
    return merge(merge_sort(left)), merge(merge_sort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))

    return result


def quick_sort(nums):
    def partition(begin, end):
        left, right = begin, end
        if left > right:
            return
        pivot = nums[left]
        while left < right:
            while left < right and nums[right] >= pivot:
                right = right-1
            while left<right and nums[left] <= pivot:
                left = left +1

            nums[left], nums[right] = nums[right], nums[left]
        nums[left], nums[begin] = pivot, nums[left]
        partition(begin, left-1)
        partition(right+1, end)

    partition(0,len(nums)-1)
    return nums

nums = [2,5,6,7,3,643,13,1,43,54,245]
# print(bubble_sort(nums))

print(quick_sort(nums))