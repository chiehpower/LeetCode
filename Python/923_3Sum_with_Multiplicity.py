"""
Given an integer array A, and an integer target, return the number of tuples i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.

As the answer can be very large, return it modulo 10^9 + 7.

Example 1:

Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (A[i], A[j], A[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: A = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.

Example 3:

Input: arr = [2,1,3], target = 6
Output: 1
Explanation: (1, 2, 3) occured one time in the array so we return 1.

Note:

- 3 <= A.length <= 3000
- 0 <= A[i] <= 100
- 0 <= target <= 300
"""
class Solution:
    def threeSumMulti(self, arr, target):
        arr.sort()
        correct = 0
        length = len(arr)
        if length < 3:
            print("The length is not enough for 3.")
            return None

        # ans = []
        
        for i in range(0, length-2):
            remain = target - arr[i]
            if remain < arr[i+1]:
                ### Cannot find a answer.
                # print("hi")
                break
            # print("remain", remain)
            for j in range(i+1, length-1):
                re_remain = remain - arr[j]
                if  re_remain < arr[j+1]:
                    # print("Break")
                    break
                for k in range(j+1, length):
                    # print(re_remain, arr[k])
                    if re_remain == arr[k]:
                        # ans.append([arr[i], arr[j], arr[k]])
                        correct += 1
        # print(ans)
        return correct


if __name__ == "__main__":
    
    Solution_923 = Solution()

    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    
    result = Solution_923.threeSumMulti(arr, target)
    print(f"My ans is: {result}\n")


    arr = [1,1,2,2,2,2]
    target = 5
    
    result = Solution_923.threeSumMulti(arr, target)
    print(f"My ans is: {result}\n")

    arr = [2,1,3]
    target = 6

    result = Solution_923.threeSumMulti(arr, target)
    print(f"My ans is: {result}\n")

    arr = [0,0,0]
    target = 0

    result = Solution_923.threeSumMulti(arr, target)
    print(f"My ans is: {result}\n")

    arr = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    target = 0

    result = Solution_923.threeSumMulti(arr, target)
    print(f"My ans is: {result}\n")