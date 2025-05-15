"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Runtime: 226 ms, faster than 95.09% of Python3 online submissions for Spiral Matrix
        Memory Usage: 20.34 MB, less than 43.23% of Python3 online submissions
        [Again]
        DFS
        Steps:
        1.	遍歷整個 grid
        2.	每當遇到 '1'，計數器 +1，並呼叫 DFS 把該島的其他 '1' 都「淹掉」或標記
        3.	走過的就變成 '0'，避免重複
        """
        if not grid:
            return 0
        
        row, col = len(grid), len(grid[0])
        count = 0
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != '1':
                return 
            grid[r][c] = '0'

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count
