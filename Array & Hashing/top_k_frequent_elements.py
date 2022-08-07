def top_k_frequent(nums, k):
    freq_dict = {}

    for num in nums:
        if num in freq_dict:
            value = freq_dict.get(num)
            freq_dict.update({num: value + 1})
        else:
            freq_dict[num] = 1

    freq_nums = []

    while len(freq_nums) != k:
        max_freq = max(freq_dict.values())
        for key in freq_dict:
            if max_freq == freq_dict[key]:
                freq_nums.append(key)
                freq_dict[key] = 0






top_k_frequent([1,1,1,2,2,3], 2)
