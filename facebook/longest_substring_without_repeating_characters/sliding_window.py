def sliding_window(s):
    hm = {}
    begin = end = 0
    size = len(s)
    longest = 0
    while end < size:
        letter = s[end]
        if letter in hm:
            longest = max(longest, end - begin)
            begin = max(hm[letter] + 1, begin)
        hm[letter] = end
        end += 1
    return max(longest, end - begin)

#s = "abcabcbb"
#s = 'pwwkew'
s = ' '
print(sliding_window(s))

'''
p, p = 0, b=0 e=1
w, w = 1, b=0, e=2
w, longest = 3




'''