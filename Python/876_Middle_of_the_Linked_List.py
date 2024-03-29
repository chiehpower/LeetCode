"""
Given the head of a singly linked list, 
return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

- Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

- Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle 
nodes with values 3 and 4, we return the second one.


Source from: LeetCode 


# Results: 

Reference:
- Good solution: 
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head):
        total = len(head)
        a = total % 2
        b = total // 2

        if a == 1:
            return head[b:]
        else:
            return head[b:]


if __name__ == "__main__":
    
    Solution = Solution()

    head = [1,2,3,4,5]
    
    result = Solution.middleNode(head)
    print(f"My ans is: {result}\n")


    head = [1,2,3,4,5,6]
    
    result = Solution.middleNode(head)
    print(f"My ans is: {result}\n")
