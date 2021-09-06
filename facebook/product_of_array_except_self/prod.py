def product_except_self(nums: list[int]) -> list[int]:
    ans = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                ans[j] *= nums[i]
        
    return ans

nums = [1,2,3,4]
[2*3*4, 1*3*4, 1*2*4, 1*2*3]
[]
print(product_except_self(nums))