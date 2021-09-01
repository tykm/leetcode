def myAtoi(s: str) -> int:
    white = True
    signed = False
    ans = ''
    for char in s:
        # Checking for leading whitespace
        if char == ' ' and white:
            continue
        else:
            white == False
            if char == '+' or char == '-':
                if signed:
                    break
                ans = char
                signed = True
                continue
            signed = True
            if not char.isalpha():
                if char == '.' or char == '+' or char == '-':
                    break
                ans += char
            else:
                break
    if ans == '' or ans == '+' or ans == '-':
        return 0
    else:
        ans = int(ans)
        if ans < -2**31:
            ans = -2**31
        elif ans > 2**31 - 1:
            ans = 2 **31 - 1
        return ans



s = '42'
t = '   -42'
u = '4193 with words'
v = 'words and 987'
w = '-91283472332'
p = '3.14'
o = '+-12'

print(myAtoi(o))