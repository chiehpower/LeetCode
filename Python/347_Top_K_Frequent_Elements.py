"""
Runtime: 238 ms, faster than 45.88% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.7 MB, less than 47.62% of Python3 online submissions for Top K Frequent Elements.
"""

class Solution:
    def topKFrequent(self, nums, k):
        if len(nums) == 1: return nums
        a = {}
        for i in nums:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        
        res = sorted(a.items(), key=lambda x:x[1], reverse=True)
        
        final_res = []
        for i in range(k):
            final_res.append(res[i][0])
        return final_res
        
            