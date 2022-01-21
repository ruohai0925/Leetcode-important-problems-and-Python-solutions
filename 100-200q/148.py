# TC: O(nlogn)
# SC:O(logn)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def sortFunc(head: ListNode, tail: ListNode) -> ListNode:
            
            if not head or not head.next:
                return head
            
            if head.next == tail:
                head.next = None
                return head

            fast = slow = head 
            while fast != tail and fast.next != tail:
                fast = fast.next.next
                slow = slow.next

            mid = slow
            return self.mergeTwoLists(sortFunc(head, mid), sortFunc(mid, tail))

        return sortFunc(head, None)            

    def mergeTwoLists(self,l1,l2): 
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
