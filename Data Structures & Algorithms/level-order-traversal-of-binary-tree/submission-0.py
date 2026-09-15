# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        distance = 0
        queue = deque()
        queue.append((root,0))

        dico = defaultdict(list)

        while queue :
            node,distance = queue.popleft()
            dico[distance].append(node.val)

            if node.left:
                queue.append((node.left,distance+1))

            if node.right:
                queue.append((node.right,distance+1))
        
        return [value for value in dico.values()]
            






            
            


                
        