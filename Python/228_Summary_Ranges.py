"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 
Constraints:
- 0 <= nums.length <= 20
- -231 <= nums[i] <= 231 - 1
- All the values of nums are unique.
- nums is sorted in ascending order.
"""
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 17.91 MB, less than 12.21% of Python3 online submissions for Summary Ranges.
        """
        res = []
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        
        total = len(nums) - 1
        count = start = nums[0]

        for i in range(total):
            if (nums[i+1] - count) == 1:
                # 連續
                count += 1
            else:
                # 非連續
                if count == start:
                    value = str(start)
                else:
                    value = str(start) + "->" + str(nums[i])
                res.append(value)
                count = start = nums[i+1]

            if i + 1 == total:
                if count == start:
                    value = str(start)
                else:
                    value = str(start) + "->" + str(nums[i+1])
                res.append(value)
                count = start = nums[i+1]
        return res

