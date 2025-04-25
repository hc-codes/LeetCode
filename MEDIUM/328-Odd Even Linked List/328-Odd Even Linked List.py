// Problem: Odd Even Linked List
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/odd-even-linked-list/
// Date: 2024-08-23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd=head
        even=head.next
        even_head=head.next
        while even and even.next:
            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next
        odd.next=even_head
        return head