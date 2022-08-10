def three_sum(nums):
    nums.sort()
    avoid_dups = set()

    # iterate through each num
    for i, num in enumerate(nums):
        # start two pointers, left after i, right end of nums
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = num + nums[left] + nums[right]
            if current_sum == 0:
                avoid_dups.add((nums[left], nums[right], num))
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    output = []

    for item in avoid_dups:
        output.append(item)

    return output

three_sum([3,0,-2,-1,1,2])

