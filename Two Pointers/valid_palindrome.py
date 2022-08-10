def is_palindrome(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())
    print(s)

    reversed_string = s[::-1]

    return reversed_string == s



def is_palindrome_2point(s):
    s = s.lower()
    s = ''.join(ch for ch in s if ch.isalnum())

    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1

    return True

is_palindrome_2point("A man, a plan, a canal: Panama")
