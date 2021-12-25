"""
Given a string s which represents an expression, 
evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. 
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in 
function which evaluates strings as mathematical expressions, 
such as eval().

- Example 1:

Input: s = "3+2*2"
Output: 7

- Example 2:

Input: s = " 3/2 "
Output: 1

- Example 3:

Input: s = " 3+5 / 2 "
Output: 5

Source from: LeetCode 


# Results: 
Runtime: 80 ms, faster than 78.40% of Python3 online submissions for Basic Calculator II.
Memory Usage: 17.2 MB, less than 13.79% of Python3 online submissions for Basic Calculator II.

Reference:
- Good solution: https://leetcode.com/problems/basic-calculator-ii/discuss/443590/python-stack
"""
from functools import reduce

### My thought is to separate by + and - , then to calculate the value by * and /
class Solution:
    def calculate(self, s):
        print(f"The string is {s}")
        s = s.replace(" ", "")
        s = s.split("+")
        new_s = []

        for i in s:
            if "-" in i:
                i = i.split("-")
                
                subtract = []
                for j in i:
                    if "/" in j or "*" in j:
                        div_num = self.cal_mul_div(j)
                    else:
                        div_num = int(j)
                    subtract.append(div_num)

                sub_num = reduce(lambda x, y: int(x) - int(y), subtract)                              
                                
                new_s.append(int(sub_num))
            else:
                subtract = []
                if "/" in i or "*" in i:
                    div_num = self.cal_mul_div(i)
                else:
                    div_num = int(i)
                new_s.append(int(div_num))
           
        sum_num = int(reduce(lambda x, y: int(x) + int(y), new_s))
            
        return sum_num
    
    def cal_mul_div(self, input_val):
        """
        Particularly handle the computation of multiplication and division.
        
        Args:
            input_val ([list])

        Returns:
            int value: output
        """
        input_val = input_val.split("*")
        num = 1
        for k in input_val:
            if len(k) != 0:
                if "/" in k:
                    k = k.split("/")
                    for jj in range(len(k)):
                        if jj == 0:
                            num = int(num * int(k[jj]))
                        else:
                            num = int(num / int(k[jj]))
                else:
                    num *= int(k)
        return int(num)

if __name__ == "__main__":
    Solution = Solution()

    s = {"3+2*2": 7,  
         " 3/2 ": 1, 
         " 3+5 / 2 ": 5, 
         " 8-6/3-1+1*2+3*4/2+5+6-4/2 ": 22, 
         "0": 0, 
         "14/3*2": 8, 
         "1+2*5/3+6/4*2": 6
         }

    for ss in s:
        result = Solution.calculate(ss)
        print(f"My ans is: {result}\n")
    
        if int(result) != s[ss]:
            raise ">>> Calculate wrong."
        else:
            print(">>> Correct.\n")