# Iteration
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # if head == None or head.next == None:
        #     return head

        dummy = ListNode(-1) # ListNode()?
        cur = dummy
        cur.next = head

        while cur.next and cur.next.next:
            nxt, tmp = cur.next, cur.next.next
            cur.next = tmp  #
            nxt.next = tmp.next
            tmp.next = nxt
            cur = nxt
        return dummy.next

# Recursion
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head == None or head.next == None:
            return head

        one = head
        two = one.next
        three = two.next

        two.next = one
        one.next = self.swapPairs(three)

        return two
