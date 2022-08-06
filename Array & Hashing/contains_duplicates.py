# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.

def contains_duplicate(nums):
    """O(n * n) solution."""
    i = 0
    j = 1

    while i < len(nums) - 1:
        if nums[i] == nums[j]:
            return True
        elif j == len(nums) - 1:
            i += 1
            j = i + 1
        else:
            j += 1

    return False


def contains_duplicate(nums):
    """O(1) solution."""
    nums_set = set(nums)
    if len(nums_set) != len(nums):
        return True
    else:
        return False