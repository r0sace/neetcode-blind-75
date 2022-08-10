def character_replacement(s, k):
    left = 0
    right = 0
    count_dict = {}
    result = -1

    while right <= len(s):

        if s[right] not in count_dict:
            count_dict[s[right]] = 1
        else:
            value = count_dict[s[right]]
            value += 1
            count_dict[s[right]] = value

        max_freq = max(count_dict.values())
        window_length = right - left + 1

        if window_length - max_freq <= k:
            if window_length > result:
                result = window_length
        else:
            while window_length - max_freq > k:
                decrement_value = count_dict[s[left]]
                decrement_value -= 1
                count_dict[s[left]] = decrement_value
                left += 1
                window_length = right - left + 1
                max_freq = max(count_dict.values())

        right += 1

    return result

character_replacement('AABABBA', 1)







