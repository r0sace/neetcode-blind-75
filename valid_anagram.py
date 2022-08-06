def is_anagram(s, t):
    string1 = ''.join(sorted(s))
    string2 = ''.join(sorted(t))

    if s == t:
        return True

    return False

def is_anagram_2(s,t):
    if len(s) != len(t):
        return False

    s_letters = {}
    t_letters = {}

    for i in range(len(s)):
        if s[i] not in s_letters:
            s_letters[s[i]] = 1
        else:
            s_count = s_letters.get(s[i]) + 1
            s_letters[s[i]] = s_count

        if t[i] not in t_letters:
            t_letters[t[i]] = 1
        else:
            t_count = t_letters.get(t[i]) + 1
            t_letters[t[i]] = t_count

    return s_letters == t_letters


