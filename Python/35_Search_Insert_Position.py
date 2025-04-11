"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

- Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

- Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

- Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums contains distinct values sorted in ascending order.
-10**4 <= target <= 10**4

Source from: LeetCode 


# Results: 

Reference:
- Good solution: 
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 18.50 MB, less than 44.77% of Python3 online submissions for Summary Ranges.
        """
        total = len(nums)
        for i in range(total):
            if target >  nums[i]:
                if i != (total -1):
                    if nums[i+1] < target:
                        continue
                    else:
                        return i + 1
                else:
                    return total
            else:
                return i

    def searchInsert_1(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += 1
                mid += 1
            else:
                right -= 1
        return mid

    def searchInsert_2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1
        
        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target: 
                return mid
            
            elif nums[mid] < target: 
                left = mid +1
            else:
                right = mid -1

        return left

if __name__ == "__main__":
    
    Solution = Solution()

    nums = [1,3,5,6]
    target = 5
    
    result = Solution.searchInsert(nums, target)
    print(f"My ans is: {result}\n")

    nums = [1,3,5,6]
    target = 2
    
    result = Solution.searchInsert(nums, target)
    print(f"My ans is: {result}\n")


    nums = [1,3,5,6]
    target = 7
    
    result = Solution.searchInsert(nums, target)
    print(f"My ans is: {result}\n")