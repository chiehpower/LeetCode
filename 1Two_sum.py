import time

class Solution:
    def twoSum(self, nums, target):
        res = []
        if len(nums) >= 2:
            a = len(nums)
            for i in range(a):
                for j in range(i+1,a):
                    sum_number = nums[i] + nums[j]
                    if sum_number == target:
                        return [i,j]
        
start = time.time()
Solution = Solution()

inputs = [1, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]
target = 18

result = Solution.twoSum(inputs, target)
print(result)

print("Time :", time.time() - start)
