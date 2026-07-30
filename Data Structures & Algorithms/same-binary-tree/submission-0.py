# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        q1 = deque([p])
        q2 = deque([q])

        while q1 or q2:
            current_p = q1.popleft()
            current_q = q2.popleft()

            if current_p is None and current_q is None:
                continue
            if current_p is None or current_q is None:
                return False
            if current_p.val != current_q.val:
                return False

            q1.append(current_p.left)
            q1.append(current_p.right)
            q2.append(current_q.left)
            q2.append(current_q.right)

        return True
