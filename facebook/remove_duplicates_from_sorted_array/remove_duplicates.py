def removeDuplicates(nums: list[int]) -> int:
    # Our first unique num is at index 0 because it's the first time we've seen it
    i = 0
    for j in range(1, len(nums)):
        # We've found a unique num for the first time
        if nums[i] != nums[j]:
            # Swap nums[i+1] with nums[j]
            i += 1
            nums[i] = nums[j]
        j += 1
    #print(nums)
    return i + 1


#nums = [1,1,2]
nums =  [0,0,1,1,1,2,2,3,3,4]
       #[0,1,0,1,1,2,2,3,3,4]
print(removeDuplicates(nums))





'''
Ideas:
    To take the dupe element and move it to the end:
        Slice array into 2 and add element to end - But this is O(n+m)...
        Multiple swaps

'''