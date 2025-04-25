// Problem: Reverse Linked List
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/reverse-linked-list/
// Date: 2024-08-23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curr=head
        prev=None
        while curr:
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        return prev