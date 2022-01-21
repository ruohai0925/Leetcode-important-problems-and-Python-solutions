    def mergeTwoLists(self, node1, node2):
        dummy = cur = ListNode()
        while node1 and node2:
            if node1.val <= node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next

        cur.next = node1 if node1 else node2
        return dummy.next # dummy.next is the head node after merging？Yes!