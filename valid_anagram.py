def is_anagram(string1, string2):
    string1 = ''.join(sorted(string1))
    string2 = ''.join(sorted(string2))

    if string1 == string2:
        return True

    return False

