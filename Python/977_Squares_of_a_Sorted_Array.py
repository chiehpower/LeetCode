"""
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

- Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

- Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order

Source from: LeetCode 


# Results: 
Runtime: 224 ms, faster than 73.02% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.4 MB, less than 12.64% of Python3 online submissions for Squares of a Sorted Array.

Reference:
- Good solution: https://leetcode.com/problems/squares-of-a-sorted-array/discuss/222079/Python-O(N)-10-lines-two-solutions-explained-beats-100
"""

class Solution:
    def sortedSquares(self, nums):
        square = lambda a: [i**2 for i in a] 

        res = square(nums)
        return sorted(res)


if __name__ == "__main__":
    
    Solution = Solution()

    nums = [-4,-1,0,3,10]
    
    result = Solution.sortedSquares(nums)
    print(f"My ans is: {result}\n")

    nums = [-7, -3, 2, 3, 11]
    
    result = Solution.sortedSquares(nums)
    print(f"My ans is: {result}\n")