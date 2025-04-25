// Problem: Delete the Middle Node of a Linked List
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
// Date: 2024-09-18

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow=head
        fast=head.next.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head