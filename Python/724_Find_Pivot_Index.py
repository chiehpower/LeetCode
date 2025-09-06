"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to 
the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because 
there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.


Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000

"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        Runtime 113ms Beats 72.09% of users with Python
        Memory 14.20MB Beats 97.79% of users with Python
        """
        sum_left = 0
        sum_right = sum(nums)
        for i in range(len(nums)):
            sum_right -= nums[i] # 直接算出右邊總合是多少
            
            if i == 0: # 如果是第0個
                if sum_left == sum_right:
                    return 0
                else:
                    # 把這個位置的數字加上下一次要計算的左邊位置上
                    sum_left += nums[i]
                    continue # 不用這個
            else:
                if sum_left == sum_right: 
                    return i
                else:
                    sum_left += nums[i]
        return -1

    def pivotIndex_20250814(self, nums: List[int]) -> int:
        # 計算陣列總和
        total = sum(nums)
        length = len(nums)
        # 用來記錄從左到右累積的總和（不包含目前 index 的值）
        check = []

        # 特殊情況：只有一個元素，必然是 pivot index
        if length == 1:
            return 0

        # 逐一檢查每個 index
        for i, value in enumerate(nums):
            if i == 0:
                # 如果是第一個元素，檢查右邊總和是否為 0
                if (total - value) == 0:
                    return i
                else:
                    # 累積左側總和
                    check.append(value)
            elif i == (length - 1):
                # 如果是最後一個元素，檢查左側總和是否為 0
                if (total - value) == 0:
                    return i
                else:
                    return -1
            else:
                # 計算剩餘的總和（扣掉目前值）
                remain = total - value
                # 右側總和 = 剩餘總和 - 左側總和
                right = remain - check[i-1]
                # 若左右總和相等，回傳目前 index
                if right == check[i-1]:
                    return i
                else:
                    # 更新左側累積總和
                    check.append(check[i-1] + value)
        # 如果都沒有符合條件，回傳 -1
        return -1

    def pivotIndex_20250907(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        total = sum(nums)
        prev = 0
        for i in range(len(nums)):
            if i == 0:
                right = total - nums[i]
                if right == 0:
                    return 0
                else:
                    prev = nums[i]
            elif i == (len(nums) -1):
                if prev == 0:
                    return i
                else: 
                    return -1
            else:
                right = total - prev - nums[i]
                if right == prev:
                    return i
                else:
                    prev += nums[i]

if __name__ == "__main__":
    
    Solution = Solution()

    nums = [1,7,3,6,5,6]

    result = Solution.pivotIndex(nums)
    print(f"My ans is: {result}\n")

    nums = [1,2,3]

    result = Solution.pivotIndex(nums)
    print(f"My ans is: {result}\n")

    nums = [2,1,-1]

    result = Solution.pivotIndex(nums)
    print(f"My ans is: {result}\n")