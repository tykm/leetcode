def valid2(s: str) -> bool:
    left = 0
    right = len(s) - 1

    if len(s) in [1,2]: return True

    while left < right:
        if s[left] != s[right]:
            return s[left + 1:right + 1] == s[left + 1:right + 1][::-1] or s[left:right] == s[left:right][::-1]
        left += 1
        right -= 1
    return True



s = "aba"
#s = 'abbca'
ss = 'abca'
sss = 'abc'
ssss = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
sssss = 'a__cupuuuupucu__a'
print(valid2(sssss))