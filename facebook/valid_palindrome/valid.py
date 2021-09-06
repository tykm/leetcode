def is_palindrome(s: str) -> bool:
    N = len(s)

    # Calculate left, right pointers
    left = 0
    right = N - 1
    skip = False
    print(left, right)
    while left < right:
        if not s[left].isalnum():
            left += 1
            skip = True
        if not s[right].isalnum():
            right -= 1
            skip = True
        if skip:
            skip = False
            continue
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
    


s = "A man, a plan, a canal: Panama"
ss = "abb:a"
ss = "abba"
sss = "abcba"

print(is_palindrome(s))