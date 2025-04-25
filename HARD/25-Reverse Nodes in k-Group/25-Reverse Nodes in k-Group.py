// Problem: Reverse Nodes in k-Group
// Difficulty: HARD
// LeetCode URL: https://leetcode.com/problems/reverse-nodes-in-k-group/
// Date: 2024-09-04

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        temp=head
        def reverse(h1):
            pre=None
            h=h1
            res=None
            while h:
                if not h.next:
                    res=h
                nxt=h.next
                h.next=pre
                pre=h
                h=nxt
            print(pre)
            return pre
        def findNode(temp,r):
            r-=1
            while temp and r>0:
                r-=1
                temp=temp.next
            return temp
        c=1
        curr=head
        pre=None
        while curr:
            k_node=findNode(curr,k)
            if not k_node:
                if pre:
                    pre.next=curr
                break
            nxt=k_node.next
            k_node.next=None
            reverse(curr)
            if curr==head:
                head=k_node
            else:
                if pre: 
                    pre.next=k_node
            pre=curr
            curr=nxt
        return head

            
            