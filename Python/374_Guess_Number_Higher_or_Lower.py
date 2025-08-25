"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.


Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        left = 1
        right = n  
        while left <= right:
            reminder = (right+left) % 2
            start = (right + left) // 2
            if reminder == 1:
                start += 1
            res = guess(start)
            if res == -1:
                right = start - 1
            elif res == 1:
                left = start + 1
            else:
                return start

    def guessNumber_20250825(self, n: int) -> int:
        left, right = 0, n 
        while left <= right:
            mid = (left + right) // 2
            res = guess(mid)
            if res == -1:
                right = mid - 1 
            elif res == 0:
                return mid
            else:
                left = mid + 1