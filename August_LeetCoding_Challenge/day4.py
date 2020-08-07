"""
# Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

#Example 1:

Input: 16
Output: true

#Example 2:

Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?

Source from: LeetCode 
"""
import time
class Solution:
    def isPowerOfFour(self, num):
        maxium = (2**31) - 1
        if num == 0:
            return False
        elif num == 1:
            return True
        elif num == 4:
            return True
        while num > 1:
            num = num / 4
            if num == 4:
                return True
        return False
      
Solution = Solution()  

### First one
inputs1 = 64

start = time.time()
result = Solution.isPowerOfFour(inputs1)
print(result)
# True
print("Time :", time.time() - start)


### Second one
inputs2 = 5
result = Solution.isPowerOfFour(inputs2)
print(result)
# False
print("Time :", time.time() - start)

### Second one
inputs3 = 144
result = Solution.isPowerOfFour(inputs3)
print(result)
# False
print("Time :", time.time() - start)
