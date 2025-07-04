"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Search a 2D Matrix.
        Memory Usage: 18.20 MB, less than 45.21% of Python3 online submissions for Search a 2D Matrix.
        """

        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1
        while left <= right:
            mid = (right + left) // 2
            row, col = divmod(mid, n)
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
                