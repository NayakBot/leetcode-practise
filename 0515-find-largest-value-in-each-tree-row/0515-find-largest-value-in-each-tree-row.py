# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cur = [root]
        toCheck = []
        res = []

        while len(cur) != 0:
            curMax = cur[0].val

            for node in cur:
                curMax = max(curMax, node.val)
                if node.left:
                    toCheck.append(node.left)
                if node.right:
                    toCheck.append(node.right)

            res.append(curMax)
            cur = toCheck
            toCheck = []
        
        return res
                