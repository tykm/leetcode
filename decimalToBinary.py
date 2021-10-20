def decToBin(dec):
    stack = []
    ans = ''
    def recur(deci):
        half = deci // 2
        r = deci % 2
        stack.append(r)
        if half > 0:
            recur(half)
    recur(dec)
    while stack:
        ans += (str(stack.pop()))
    return ans

print(decToBin(19))


'''
9
1 0 0 1

13
1 1 0 1
13//2 = 6r1
6//2 = 3r0
3//2 = 1r1
1//2 = 0r1

17
1 0 0 0 1
1
'''