"""
Given a 0-indexed n x n integer matrix grid, 
return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain 
the same elements in the same order (i.e., an equal array).

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        col_list = []
        row_list = []
        row_number = len(grid[0])
        
        for i in range(row_number):
            value = '' 
            for j in grid[i]:
                value += str(j) + ','
            row_list.append(value)
        
        for i in range(row_number):
            value = ''
            for j in range(row_number):
                value += str(grid[j][i])  + ','
            col_list.append(value)

        count = {}
        for i in row_list:
            for j in col_list:
                if i == j:
                    if i not in count:
                        count[i] = 1
                    else:
                        count[i] += 1

        all_values = count.values()
        max_value = 0

        for i in all_values:
            if i > 0:
                max_value += i

        return max_value