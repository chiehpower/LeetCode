"""
Given an array of intervals where intervals[i] = [start_i, end_i], 
merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

- Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

- Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= start_i <= end_i <= 10^4

# Results: 
Runtime: 1748 ms, faster than 5.09% of Python3 online submissions for Merge Intervals.
Memory Usage: 16.2 MB, less than 54.81% of Python3 online submissions for Merge Intervals.

Reference:
- Good solution: https://leetcode.com/problems/merge-intervals/discuss/1644409/C%2B%2BPython-Simple-Solutions-w-Explanation-or-Sort-Merge-O(NlogN)-%2B-Count-Sort-O(N-%2B-R)
"""

class Solution:
    def merge(self, intervals):
        intervals.sort()
        new_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= new_intervals[-1][1]:
                new_intervals[-1] = [new_intervals[-1][0], max(intervals[i][1], new_intervals[-1][1])]
            else:
                new_intervals.append(intervals[i])
            intervals.sort()
        return new_intervals

if __name__ == "__main__":
    Solution = Solution()
    import time

    tasks = [[[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 4], [4, 5]], [[1, 6]],
         [[12, 100], [90, 92], [1, 9], [2, 8],
         [111, 116], [109, 115]], [[1, 4], [0, 2], [3, 5]]]
    for intervals in tasks:
        s = time.time()
        print(f"Task is {intervals}")
        result = Solution.merge(intervals)
        print("Spend: ", time.time() - s)
        print(f"My ans is: {result}\n")
        

    ## first one 
    ## [[1,6],[8,10],[15,18]]

    ## second 
    ## [[1,5]]

    ## third 
    ## [[1,6]]
    
    ## fourth 
    ## [[1, 9], [12, 100], [109, 116]]
    
    ## fifth
    ## [[0,5]]