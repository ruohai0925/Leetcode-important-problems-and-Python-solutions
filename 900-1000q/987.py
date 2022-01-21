class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.res = []  # Combine val,row,col into a term in list, res is a list of list

        def dfs(root, row, col):
            if not root:
                return
            self.res.append([root.val, row, col])  # append
            dfs(root.left, row + 1, col - 1)
            dfs(root.right, row + 1, col + 1)

        def bfs(root):
            q = deque()
            q.append([root, 0, 0])  # append
            while q:
                cur, r, c = q.popleft()
                self.res.append([cur.val, r, c])
                if cur.left:
                    q.append([cur.left, r + 1, c - 1])
                if cur.right:
                    q.append([cur.right, r + 1, c + 1])

        # dfs(root, 0, 0)
        bfs(root)
        self.res.sort(key=lambda x: (x[2], x[1], x[0]))  # sort many elements, col: left -> right, row: top -> bottom, val: small -> large
        res = [[self.res[0][0]]]
        for i in range(1, len(self.res)):  # loop all nodes
            if self.res[i][2] == self.res[i - 1][2]:
                res[-1].append(self.res[i][0])  # add one value in the last term
            else:
                res.append([self.res[i][0]])  # add one more term
        return res
