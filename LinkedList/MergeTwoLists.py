# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # input: heads of two lists to be merged
        # output: head of merged list
        # goal: compare and merge two lists
        # solution
        # 1. loop thru shorter list
        # 2. compare node1 with node2 
        # 3. if node1 > node2, compare node2.next
        # 4. if node1 < node2, node1 points to node2
        list3 = ListNode()
        tail = list3
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        tail.next = list1 or list2
        return list3.next

