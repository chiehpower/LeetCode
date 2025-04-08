"""
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

Example 2:

Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""
from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Summary Ranges.
        Memory Usage: 19.90 MB, less than 43.86% of Python3 online submissions for Summary Ranges.

        是利用deque來做BFS的方式
        1. 先把root放進deque裡面
        2. 開始進行BFS的過程
        3. 每一層都會有一個max_len的變數來計算本層有多少個node
        4. 每一層都會有一個max_sum的變數來計算本層所有node的總和
        5. 每一層都會有一個ave的變數來計算本層所有node的平均值
        6. 每一層都會把計算出來的ave放進result裡面
        7. 當deque裡面沒有node的時候，代表BFS結束了
        8. 最後把result回傳
        """
        result = []
        d = deque([root])
        while d:
            max_len = len(d) # 計算本層總共有多少個node
            max_sum = 0
            for _ in range(max_len):
                node = d.popleft() # 開始移除本層每一個需要計算的node
                max_sum += node.val

                if node.left:
                    d.append(node.left) # 把這個node的左子node加入

                if node.right:
                    d.append(node.right) # 把這個node的右子node加入

            ave = max_sum / max_len
            result.append(ave)
        return result
                
