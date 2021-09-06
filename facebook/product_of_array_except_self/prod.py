def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [1] * n
    for i in range(n-1):
        ans[i+1] = nums[i] * ans[i]
    for i in range(n-1, 0, -1):
        ans[i-1] = ans[i-1] * nums[i]
        nums[i-1] = nums[i-1] * nums[i]
    return ans

nums =  [1     , 2      , 3      , 4     ]
     #  [1     , 1      , 1      , 1     ]
     #  [1     , 1      , 1*2    , 1*2*3 ]
     #  [ 2*3*4, 1 * 3*4, 1*2 * 4, 1*2*3 ]
[]
print(product_except_self(nums))