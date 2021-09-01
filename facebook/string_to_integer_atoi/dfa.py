def myAtoi(s: str) -> int:
    ans = 0
    signed = False
    neg = False
    white = True
    for c in s:
        # Leading whitespace
        if c == ' ' and white:
            continue
        else:
            white = False
            # + or -
            if c == '+' and not signed:
                signed = True
            elif c == '-' and not signed:
                neg = signed = True
            elif c.isdigit():
                signed == True
                ans = ans * 10 + int(c)
            else:
                signed == True
                break
    if signed and neg:
        ans *= -1
    if ans < -2**31:
        ans = -2**31
    elif ans > 2**31 - 1:
        ans = 2**31 - 1
            
    return ans



s = '42'
t = '   -42'
u = '4193 with words'
v = 'words and 987'
w = '-91283472332'
p = '3.14'
o = '+-12'
z = '    +  35'

print(myAtoi(z))