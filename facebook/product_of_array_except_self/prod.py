def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    ans = [1] * n
    for i in range(n):
        print(nums[n-i-1])
        
        
    return ans

nums = [1,2,3,4]
[ 2*3*4, 1 * 3*4, 1*2 * 4, 1*2*3 ]
[]
print(product_except_self(nums))