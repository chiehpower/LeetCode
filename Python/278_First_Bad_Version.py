"""
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. 
Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.



- Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

- Example 2:

Input: n = 1, bad = 1
Output: 1

Source from: LeetCode 


# Results: 
Runtime: 32 ms, faster than 50.27% of Python3 online submissions for First Bad Version.
Memory Usage: 14.1 MB, less than 91.21% of Python3 online submissions for First Bad Version.

Reference:
- Good solution: https://leetcode.com/problems/first-bad-version/discuss/769685/Python-Clear-explanation-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def isBadVersion(version, bad):
    # bad = 2
    if version>=bad:
        return True
    else:
        return False

# class Solution:
#     """12/26/2021 22:50"""
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         max_ = n
#         min_ = 1
#         if max_ == min_:
#             return max_
#         while min_ < max_:
#             mid = int((max_ + min_) / 2)
#             res = isBadVersion(mid)  # False (no problem)
#             if res:
#                 ## problem
#                 if isBadVersion(mid-1) == False:
#                     return mid
#                 else:
#                     max_ = mid
#             else:
#                 if isBadVersion(mid+1):
#                     return mid+1
#                 else:
#                     min_ = mid+1


class Solution:
    def firstBadVersion(self, n, bad):       
        """
        Runtime: 44 ms, faster than 57.81% of Python3 online submissions for First Bad Version.
        Memory Usage: 13.9 MB, less than 13.13% of Python3 online submissions for First Bad Version.
        """
        if n == 1: return 1
        max_ = n
        min_ = 1    
        while min_ < max_:
            ### Step : 
            ### 1. Calculate middle value > check whether it is True of False.
            ### 2. If True, then find the left way. 
            ### 3. If False, then find the right way.

            middle = int((max_ + min_) / 2)
            res = isBadVersion(middle, bad)
            if res:
                if middle == 1: return 1
                max_ = middle
            else:
                if isBadVersion(middle + 1, bad):
                    ## later one is badversion
                    return middle + 1
                else:
                    min_ = middle


if __name__ == "__main__":
    Solution = Solution()

    n = 5
    bad = 4

    print(f"Number is {n}, and bad {bad}")
    result = Solution.firstBadVersion(n, bad)
    print(f"My ans is: {result}\n")

    n = 1
    bad = 1

    print(f"Number is {n}, and bad {bad}")
    result = Solution.firstBadVersion(n, bad)
    print(f"My ans is: {result}\n")

    n = 2
    bad = 2

    print(f"Number is {n}, and bad {bad}")
    result = Solution.firstBadVersion(n, bad)
    print(f"My ans is: {result}\n")

    n = 2
    bad = 1

    print(f"Number is {n}, and bad {bad}")
    result = Solution.firstBadVersion(n, bad)
    print(f"My ans is: {result}\n")
