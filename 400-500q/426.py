# recursive
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return  
        self.head = None
        self.prev = None  
        self.dfs(root)

        self.prev.right = self.head 
        self.head.left = self.prev
        return self.head

    # in-order
    def dfs(self, curr):
        if not curr:
            return 
        self.dfs(curr.left)
        if not self.head:
            self.head = curr
        if self.prev:
            self.prev.right = curr  
            curr.left = self.prev
        self.prev = curr 
        self.dfs(curr.right)
# TC：O(n)
# SC: O(n)

# iterative
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return

        head = None
        prev = None  
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
        
            curr = stack.pop()

            if not prev:
                head = curr 
            else:
                prev.right = curr  
                curr.left = prev
            prev = curr 
            curr = curr.right

        prev.right = head 
        head.left = prev
        return head
