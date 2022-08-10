def length_of_longest_substring(s):
    character_set = set()
    left = 0
    temp_count = 0
    count = 0

    for r in range(len(s)):
        while s[r] in character_set:
            character_set.remove(s[left])
            left += 1
        character_set.add(s[r])
        temp_count = r - left + 1
        if temp_count > count:
            count = temp_count

    return count



length_of_longest_substring('qrsvbspk')