// Problem: Palindrome Linked List
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/palindrome-linked-list/
// Date: 2024-08-23

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt
        curr=head
        pal=False
        while curr and prev:
            # print(prev.val, curr.val)
            if curr.val!=prev.val:
                return False
            else:
                pal=True
            curr=curr.next
            prev=prev.next
        # print(curr,prev)
        if pal: 
            return True
        return False