def contains_duplicate(nums):
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
    nums_set = set(nums)
    if len(nums_set) != len(nums):
        return True
    else:
        return False