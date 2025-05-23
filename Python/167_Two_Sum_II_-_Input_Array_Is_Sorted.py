"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        total = len(numbers)
        for i in numbers:
            remain = target - i
            new_numbers = numbers[left_pointer+1:]
            try:
                right_pointer = new_numbers.index(remain)
            except:
                left_pointer += 1
                continue
            return [left_pointer+1, left_pointer+1 + right_pointer+1]

    def twoSum_two_pointers(self, numbers: List[int], target: int) -> List[int]:
        left_pointer, right_pointer = 0, len(numbers) - 1
        while left_pointer < right_pointer:
            current_value = numbers[left_pointer] + numbers[right_pointer]
            if current_value == target: 
                return [left_pointer+1, right_pointer+1]
            elif current_value < target:
                left_pointer += 1
            else:
                right_pointer -= 1

new_numbers = [2,7,11,15]
target = 9
Solution = Solution()
print(Solution.twoSum_two_pointers(new_numbers, target)) # Answer: [1, 2]

new_numbers = [2,3,4]
target = 6
Solution = Solution()
print(Solution.twoSum_two_pointers(new_numbers, target)) # Answer: [1, 3] 

new_numbers = [-1,0]
target = -1
Solution = Solution()
print(Solution.twoSum_two_pointers(new_numbers, target)) # Answer: [1, 2]

new_numbers = [5,25,75]
target = 100
Solution = Solution()
print(Solution.twoSum_two_pointers(new_numbers, target)) # Answer: [2, 3]