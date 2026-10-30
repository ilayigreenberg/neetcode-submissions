# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        nodeOrder = {root : [float('-inf'), float('inf')]}

        while q:
            node = q.popleft()
            left, right = node.left, node.right

            if left:
                if not (nodeOrder[node][0] < left.val < node.val):
                    return False
                q.append(left)
                nodeOrder[left] = [nodeOrder[node][0], node.val]
                
            if right:
                if not (node.val < right.val < nodeOrder[node][1]):
                    return False
                q.append(right)
                nodeOrder[right] = [node.val, nodeOrder[node][1]]             

        return True