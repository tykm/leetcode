def sliding_window(s):
    hm = {}
    begin = end = 0
    size = len(s)
    longest = 1
    while end < size:
        curr_letter = s[end]
        if hm.get(curr_letter):
            longest = max(longest, end - begin)
            begin = end + 1
            hm = {}
        else:
            hm[curr_letter] = True
        end += 1 
    return longest

s = "abcabcbb"
s = 'pwwkew'
print(sliding_window(s))