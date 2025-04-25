// Problem: Intersection of Two Linked Lists
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/intersection-of-two-linked-lists/
// Date: 2024-08-30

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return
        c1=headA
        c2=headB
        l1=None
        l2=None
        while c1 and c2:
            if not c1.next and not c2.next:
                return None if c1!=c2 else c1
            if not c1.next:
                c1=headB
                c2=c2.next
                continue
            if not c2.next:
                c2=headA
                c1=c1.next
                continue
            if c1==c2:
                return c1
            c1=c1.next
            c2=c2.next
        return None