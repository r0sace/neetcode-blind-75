def is_anagram(s, t):
    string1 = ''.join(sorted(s))
    string2 = ''.join(sorted(t))

    if s == t:
        return True

    return False

