'''
Rotate Image Leetcode
3x3
0,0 = 0,2
0,1 = 1,2
0,2 = 2, 2

1,0 = 0,1
1,1 = 1,1
1,2 = 2,1

2,0 = 0,0
2,1 = 1,0
2,2 = 2,0

equation to rotate n*n 90 degrees
x,y  => y, max-x
where max = n

4x4
1,1 = 1,2
1,2 = 2,2
0,0 = 0,3
0,1 = 1,,3
2,0 = 0,1
2,1 = 1,1
'''

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix) - 1
        
        # Function to return new coordinates
        def rot(x, y):
            return y, n-x
        
        for col in range((n+1)//2):
            for row in range(col, n):
                first_col, first_row = rot(col, row)
                second_col, second_row = rot(first_col, first_row)
                third_col, third_row = rot(second_col, second_row)
                #print(col, row, first_col, first_row, second_col, second_row, third_col, third_row)
                curr = matrix[col][row]
                first = matrix[first_col][first_row]
                second = matrix[second_col][second_row]
                third = matrix[third_col][third_row]
                #print(curr, first, second, third)
                matrix[col][row] = third
                matrix[first_col][first_row] = curr
                matrix[second_col][second_row] = first
                matrix[third_col][third_row] = second