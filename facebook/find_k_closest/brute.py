def find(arr: list[int], k: int, x: int) -> list[int]:
    distances = []
    low = float('inf')
    mid = len(arr) + 1
    for i in range(len(arr)):
        dist = abs(arr[i] - x)
        distances.append(dist)
        if dist < low:
            low = dist
            mid = i

    left = right = mid
    
    while right-left + 1 < k:
        if distances[left - 1] <= distances[right + 1]:
            left -= 1
        else:
            right += 1
        # If we're out of bounds:
        if left < 0:
            return arr[left+1:right+1+k-right+1]
        elif right > len(arr) - 1:
            return arr[left-k-left+1:right-1]
            
            
    
    return arr[left:right+1]
            
        
    
    
    
arr = [1,2,3,4,5]
k = 4
x = 3
# Output: [1,2,3,4]
arr = [-2,-1,1,2,3,4,5]
k = 7
x = 3

print(find(arr, k, x))