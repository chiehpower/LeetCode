"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 
Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        """
        Runtime: 78 ms, faster than 33.09% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 14 MB, less than 33.04% of Python3 online submissions for Merge Two Sorted Lists.
        ref: https://www.youtube.com/watch?v=Z7VOBq6S5n8
        """
        ## Same or not same 
        current = dummy = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else: 
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        current.next = list1 or list2
        
        return dummy.next

    def 20250504(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Again
        - 20250505
        - 20250506
        """
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        current.next = list1 if list1 else list2

        return dummy.next