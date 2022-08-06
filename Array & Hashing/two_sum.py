def two_sum(nums, target):
    prevMap = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i



def two_sum2(nums, target):
    for pointer_one in range(len(nums)-1):
        i = nums[pointer_one]
        for pointer_two in range(pointer_one+1, len(nums)):
            j = nums[pointer_two]
            if i + j == target:
                return pointer_one, pointer_two
