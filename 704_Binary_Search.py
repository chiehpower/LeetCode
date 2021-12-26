"""
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

- Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

- Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Source from: LeetCode 


# Results: 
Runtime: 228 ms, faster than 91.77% of Python3 online submissions for Binary Search.
Memory Usage: 15.6 MB, less than 28.71% of Python3 online submissions for Binary Search.

Reference:
- Good solution: https://leetcode.com/problems/binary-search/discuss/1642864/python3-implementation
"""

class Solution:
    def search(self, nums, target):
        stop = True
        cp_nums = nums.copy()
        index = len(nums) - 1
        if target not in nums:
            return -1
        while stop:
            total = len(cp_nums)
            half = int(total/2)

            if cp_nums[half] == target:
                index = nums.index(cp_nums[half])
                return index
            elif len(cp_nums) == 1 and cp_nums[half] != target:
                return -1
            elif cp_nums[half] > target:
                cp_nums = cp_nums[:half]
                index -= len(cp_nums)
            else:
                cp_nums = cp_nums[half:]
                index += len(cp_nums)
            
                
if __name__ == "__main__":
    Solution = Solution()
    
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    
    print(f"Number is {nums}, and target {target}")
    result = Solution.search(nums, target)
    print(f"My ans is: {result}\n")

    nums = [-1, 0, 3, 5, 9, 12]
    target = -1
    
    print(f"Number is {nums}, and target {target}")
    result = Solution.search(nums, target)
    print(f"My ans is: {result}\n")
