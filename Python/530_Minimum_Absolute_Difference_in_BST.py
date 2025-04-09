"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1
 
Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Runtime: 6 ms, faster than 38.60% of Python3 online submissions for Summary Ranges.
        Memory Usage: 19.71 MB, less than 25.06% of Python3 online submissions for Summary Ranges.

        Note: need to write again
        """
        self.min_value = float('inf')
        self.previous_node = None

        def inorder(node):
            if not node:
                return 

            # 先走訪左邊
            inorder(node.left)
            
            # 跟前面一個比較
            if self.previous_node is not None:
                self.min_value = min(self.min_value, abs(node.val - self.previous_node))
            
            self.previous_node = node.val

            # 走訪右邊
            inorder(node.right)
        
        inorder(root)
        return self.min_value