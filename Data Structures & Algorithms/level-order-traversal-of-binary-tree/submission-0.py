# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        qeue = collections.deque()
        qeue.append(root)

        while qeue:
            lenq = len(qeue)
            level=[]
            for i in range(lenq):
                x = qeue.popleft()
                if x:
                    level.append(x.val)
                    qeue.append(x.left)
                    qeue.append(x.right)
            if level:
                res.append(level)
        return res


            