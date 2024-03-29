# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = Counter()
        
        def dfs(node):
            if node:
                counter[node.val] += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)

        max_ct = counter.most_common(1)[0][1]

        return [k for k, v in counter.items() if v == max_ct]