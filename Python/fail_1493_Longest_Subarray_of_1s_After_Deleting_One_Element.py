"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing 
only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, 
[1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, 
[0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        This answer was checked by the solution.
        """
        max_length = 0  # Initialize the maximum length to 0.
        left = 0  # Initialize the left pointer of the sliding window.
        count_zeros = 0  # Initialize a count for zeros in the current window.

        for right in range(len(nums)):
            if nums[right] == 0:
                count_zeros += 1  # Increment the count of zeros.

            # If there are more than one zero in the current window, move the left pointer.
            print("Nums[right]: {}".format(nums[right]))
            while count_zeros > 1:
                if nums[left] == 0:
                    count_zeros -= 1
                    print("count_zeros: {}".format(count_zeros))

                left += 1
                print(left)

            # Calculate the maximum length of the subarray.
            max_length = max(max_length, right - left)

        # If there are no zeros in the input array, return len(nums) - 1
        if max_length == len(nums):
            return max_length - 1

        # Otherwise, return max_length
        return max_length