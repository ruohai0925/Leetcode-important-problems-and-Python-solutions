class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = collections.deque()
        queue.append((root,0))
        lookup = collections.defaultdict(list) # Using list as the default_factory, it is easy to group a sequence of key-value pairs into a dictionary of lists. Also, dic = defaultdict(int) represents the dic value is int
        res = []

        while queue:
            for _ in range(len(queue)):
                node, column = queue.popleft()
                lookup[column].append(node.val) 

                if node.left:
                    queue.append((node.left, column - 1))
                if node.right:
                    queue.append((node.right, column + 1))

        l = min(lookup.keys()) # keys()
        r = max(lookup.keys())

        for i in range(l, r+1):
            res.append(lookup[i])

        return res
