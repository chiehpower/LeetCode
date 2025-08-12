"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        """
        Runtime: 69 ms, faster than 44.48% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.5 MB, less than 55.12% of Python3 online submissions for Reverse Linked List.
        
        Ref: https://leetcode.com/problems/reverse-linked-list/discuss/58127/Python-Iterative-and-Recursive-Solution
        """
        if head == None: return head
        prev = None
        while head:
            current = head 
            head = head.next
            current.next = prev
            prev = current
            
        return current

    def reverseList_20230824(self, head):
        """
        Runtime: 23 ms, faster than 41.73% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.27 MB, less than 57.38% of Python3 online submissions for Reverse Linked List.
        
        2025/05/30 
        """
        
        prev = None
        current = head

        while current is not None:
            next_node = current.next # 暫存下一個節點
            current.next = prev # 把當前節點指回前一個 → ★反轉的核心
            prev = current # 移動 prev 指向 curr（下次使用）
            current = next_node # 移動 curr 繼續走
        return prev

    def reverseList20250812(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        record = []
        while head:
            record.append(head.val)
            head = head.next
        record.reverse()
        root = ListNode()
        pointer = root
        for i in record:
            pointer.next = ListNode(i)
            pointer = pointer.next
        return root.next