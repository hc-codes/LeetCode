// Problem: Symmetric Tree
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/symmetric-tree/
// Date: 2023-08-15

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
        
    def isMirror(self, left, right):
        if left == None and right == None:
            return True
        elif left ==None or right ==None:
            return False
        
        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPiar = self.isMirror(left.right, right.left)
            return outPair and inPiar
        else:
            return False