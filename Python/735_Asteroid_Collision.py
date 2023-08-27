"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the 
sign represents its direction (positive meaning right, 
negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, 
both will explode. Two asteroids moving in the same direction will never meet.

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. 
The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        col = [asteroids[0]]
        for i in asteroids[1:]:
            if len(col) == 0:
                col.append(i)
                continue
            if col[-1] > 0:
                if i > 0:
                    col.append(i)
                else:
                    ok = True
                    while ok:
                        print(col[-1])
                        if col[-1] > 0 and (abs(col[-1]) > abs(i)):
                            break
                        elif col[-1] > 0 and (abs(col[-1]) == abs(i)):
                            col.pop()
                            break
                        elif col[-1] > 0 and (abs(col[-1]) < abs(i)):
                            col.pop()
                            if len(col) == 0:
                                col.append(i)
                                break
                        elif col[-1] < 0:
                            col.append(i)
                            break
            else:
                col.append(i)
        return col

if __name__ == "__main__":
    
    Solution = Solution()
    
    asteroids = [5,10,-5]

    result = Solution.asteroidCollision(asteroids)
    print(f"My ans is: {result}\n")

    asteroids = [8,-8]

    result = Solution.asteroidCollision(asteroids)
    print(f"My ans is: {result}\n")

    asteroids = [10,2,-5]

    result = Solution.asteroidCollision(asteroids)
    print(f"My ans is: {result}\n")

    asteroids = [-2,-1,1,2]

    result = Solution.asteroidCollision(asteroids)
    print(f"My ans is: {result}\n")

    asteroids = [-2,-2,1,-2]

    result = Solution.asteroidCollision(asteroids)
    print(f"My ans is: {result}\n")

    asteroids = [1,-1,-2]

    result = Solution.asteroidCollision(asteroids)
    print(f"My ans is: {result}\n")
