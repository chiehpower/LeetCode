"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
import time

class Solution:
    def longestCommonPrefix(self, common):
        num = len(common)
        if num == 0:
            return ""

        if num == 1:
            return common[0]

        fir = ""
        word = len(common[0])
        for i in range(word):
            for j in range(1, num):
                try:
                    if common[j][i] != common[0][i]:
                        return fir
                except:
                    return fir
            fir += common[0][i]
        return fir

    def longestCommonPrefix_2loops(self, strs: List[str]) -> str:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Spiral Matrix.
        Memory Usage: 18.04 MB, less than 8.03% of Python3 online submissions for Spiral Matrix.
        """
        min_value = len(strs[0])
        for i in strs:
            if len(i) < min_value:
                min_value = len(i)
        
        prefix = ""
        stop = False
        for j in range(min_value):
            pre = strs[0][j]
            for k in strs:
                if pre != k[j]:

                    stop = True
                    break
            if stop:
                break
            prefix += pre
        
        return prefix

if __name__ == "__main__":
    Solution = Solution()

    ### First one
    strs = ["flower", "flow", "flight"]

    start = time.time()
    result = Solution.longestCommonPrefix(strs)
    print(result)

    print("Time :", time.time() - start)
    if result != "fl":
        print("Example 1 got a wrong answer.")
    else:
        print("Example 1 Correct!")

    ### Second one
    strs = ["dog", "racecar", "car"]

    start = time.time()
    result = Solution.longestCommonPrefix(strs)
    print(result)

    print("Time :", time.time() - start)
    if result != "":
        print("Example 2 got a wrong answer.")
    else:
        print("Example 2 Correct!")

    ### Third one
    strs = ["ab", "a"]

    start = time.time()
    result = Solution.longestCommonPrefix(strs)
    print(result)

    print("Time :", time.time() - start)
    if result != "a":
        print("Example 3 got a wrong answer.")
    else:
        print("Example 3 Correct!")
