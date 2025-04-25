// Problem: Add Two Numbers
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/add-two-numbers/
// Date: 2024-09-30

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
             return l1
        dummy=ListNode(-1)
        curr=dummy
        carry=0
        while l1 or l2:
            s=carry
            if l1:
                s+=l1.val
                l1=l1.next
            if l2:
                s+=l2.val
                l2=l2.next
            node=ListNode(s%10)
            carry=s//10
            curr.next=node
            curr=curr.next
        if carry!=0:
            curr.next=ListNode(carry)
        return dummy.next