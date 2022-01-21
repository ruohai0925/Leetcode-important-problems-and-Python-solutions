# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heapify, heappop, heappush
class Solution:
def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        n = len(lists)
        if n == 0: return None
        if n == 1: return lists[0]23

        dummy = cur = ListNode()
        minheap = []
        heapify(minheap)
        for i in range(n):
            if lists[i]: 
                heappush(minheap, (lists[i].val, i))
                print(i, lists[i], minheap)  
                lists[i] = lists[i].next
        print(minheap)
        while minheap:
            mini_val, mini_index = heappop(minheap)
            cur.next = ListNode(mini_val)
            cur = cur.next
            if lists[mini_index]:
                heappush(minheap, (lists[mini_index].val, mini_index))
                lists[mini_index] = lists[mini_index].next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)

    def merge(self, lists, left, right): #（recursive）+ (merge)
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self,l1,l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
