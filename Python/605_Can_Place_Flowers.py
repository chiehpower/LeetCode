"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, 
and an integer n, return true if n new flowers can be planted 
in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool

        Runtime 117ms Beats 87.73% of users with Python
        Memory 13.96mb Beats 53.52% of users with Python
        """
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            elif flowerbed[0] == 1 and n == 0:
                return True
            elif flowerbed[0] == 0 and n == 0:
                return True
            else:
                return False
        count = 0
        total = len(flowerbed)
        last = 0
        for i in range(total):
            if i == 0:
                # Deal with the first index situation.
                if flowerbed[i] == 0:
                    if flowerbed[i+1] == 0:
                        count += 1
                        last = 1
                        # if count == n:
                        #     return True
                        # else:
                        #     return False
                    else:
                        last = 0
                else:
                    last = 1
                continue

                
            if (i + 1) == total:
                if last == 0:
                    if flowerbed[i] == 0:
                        count += 1
                        last = 1
                        # if count == n:
                        #     return True
                        # else:
                        #     return False
                continue

            if flowerbed[i] == 1:
                last = 1
                continue
            else:
                if last == 0 and flowerbed[i+1] == 0:
                    count += 1
                    last = 1
                    # if count == n:
                    #     return True
                    # else:
                    #     return False

                    continue
                else:
                    last = 0
                
        if count >= n:
            return True
        else:
            return False
            
    
if __name__ == "__main__":
    
    Solution = Solution()

    flowerbed = [1,0,0,0,1]
    n = 1
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")
    
    flowerbed = [1,0,0,0,1]
    n = 2
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")

    candies = [1,0]
    extraCandies = 1
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")


    candies = [1,0,0]
    extraCandies = 1
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")


    candies = [1,0,1]
    extraCandies = 1
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")


    candies = [1,0,0,0,0,1]
    extraCandies = 2
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")

    candies = [1]
    extraCandies = 1
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")

    candies = [0,0,1,0,0]
    extraCandies = 1
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")


    candies = [0]
    extraCandies = 0
    
    result = Solution.canPlaceFlowers(flowerbed, n)
    print(f"My ans is: {result}\n")
