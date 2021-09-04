def removeDuplicates(nums: list[int]) -> int:
    i = 0
    for j in range(1, len(nums)):
        print(j)
    
    return i


#nums = [1,1,2]
nums =  [0,0,1,1,1,2,2,3,3,4]
       #[0,1,0,1,1,2,2,3,3,4]
removeDuplicates(nums)





'''
Ideas:
    To take the dupe element and move it to the end:
        Slice array into 2 and add element to end - But this is O(n+m)...
        Multiple swaps

'''