def longest_consecutive(nums):
    if len(nums) == 0:
        return 0

    nums.sort()
    temp = 1
    consec_count = 0

    for i in range(len(nums) - 1):
        if nums[i + 1] == nums[i] + 1:
            temp += 1
        elif nums[i + 1] == nums[i]:
            temp = temp
        else:
            if temp > consec_count:
                consec_count = temp
            temp = 1

    if consec_count < temp:
        consec_count = temp

    return consec_count

longest_consecutive([9,1,4,7,3,-1,0,5,8,-1,6])