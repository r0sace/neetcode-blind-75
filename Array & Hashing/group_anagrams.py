def group_anagrams(strings):
    strings_dict = {}

    for i, string in enumerate(strings):
        string_sorted = ''.join(sorted(string))
        if string_sorted in strings_dict:
            value = strings_dict.get(string_sorted)
            value.append(strings[i])
        else:
            strings_dict[string_sorted] = [strings[i]]

    anagrams = []
    for key in strings_dict:
        anagram_group = strings_dict[key]
        anagrams.append(anagram_group)

    return anagrams




group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
