class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        left = right = 0
        fruit2_location = None
        fruit1 = fruit2 = None
        
        # Loop through all fruits with l,r pointers
        while right < len(fruits):
            # When we encounter a fruit
            fruit = fruits[right]
            
            # Check if we have a defined basket for the fruit
            #if fruit == fruit1 or fruit == fruit2:
            #    continue
                
            # If else check if we have an empty basket for the fruit
            if fruit1 == None:
                fruit1 = fruit
                left = right
            elif fruit2 == None and fruit != fruit1:
                fruit2 = fruit
                fruit2_location = right
            
            # If else, this means we have a third fruit. Check if third fruit fits within our baskets.
            elif fruit1 == fruit or fruit2 == fruit:
                if fruit == fruit2 and fruit != fruit1:
                    fruit2_location = right
                pass
            
            # Else, this means we have a completely new fruit. Let's set the left pointer to the first location of the second fruit and continue
            else:
                fruit1 = fruit2
                fruit2 = fruit
                left = fruit2_location
                fruit2_location = right
                                    
            if right - left + 1 > max_fruits:
                max_fruits = right - left + 1
            print(left,right,max_fruits)
            right += 1


            
        return max_fruits