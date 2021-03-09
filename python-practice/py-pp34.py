https://leetcode.com/problems/same-tree/
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        
        if p is None:
            return False
        if q is None:
            return False
        
        stack = deque()
        stack.append((p, q))
        
        while stack:
            p, q = stack.pop()
            
            if p.val != q.val:
                return False
            
            if p.left and q.left:
                stack.append((p.left, q.left))
            elif p.left or q.left:
                return False
            
            if p.right and q.right:
                stack.append((p.right, q.right))
            elif p.right or q.right:
                return False
            
        return True