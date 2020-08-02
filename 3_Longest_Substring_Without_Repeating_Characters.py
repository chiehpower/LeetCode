"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Source from: LeetCode 
"""
import time 

class Solution:
    def lengthOfLongestSubstring(self, s):
        strtolist = list(s)
        res1 = []
        res2 = []
        res1count = 0
        res2count = 0
        for i in strtolist:
            if i not in res1:
                res1.append(i)
                if len(res1) > len(res2):
                        res2 = res1
            else:
                if len(res1) > len(res2):
                    res2 = res1 
                    res1 = res1[ res1.index(i) +1 :]
                    res1.append(i)
                else:
                    res1 = res1[ res1.index(i) +1 :]
                    res1.append(i)
        return len(res2)



Solution = Solution()  

### First one
inputs1 = "abcabcbb"

start = time.time()
result = Solution.lengthOfLongestSubstring(inputs1)
print(result)

print("Time :", time.time() - start)
        
### Second
inputs2 = "bbbbb"

start = time.time()
result = Solution.lengthOfLongestSubstring(inputs2)
print(result)

print("Time :", time.time() - start)

### Third
inputs3 = "pwwkew"

start = time.time()
result = Solution.lengthOfLongestSubstring(inputs3)
print(result)

print("Time :", time.time() - start)

### Fourth
inputs4 = "dvdf"

start = time.time()
result = Solution.lengthOfLongestSubstring(inputs4)
print(result)

print("Time :", time.time() - start)