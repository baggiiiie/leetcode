from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input: head of a linked list (a node)
        # output: head of a linked list (the last node of input)
        # goal: reverse the list, make each node's next point to its prev
        # solution:
        # 1. temp to save prev, first node points to None, subsequential nodes points to temp
        # 2. go to the next node, stop when the node's next pointer is null, 
        # 3. return the last node
        curr_node, prev_node = head, None
        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        return prev_node

            
        
if __name__ == '__main__':
    solution = Solution()
    vals = [0,1,2,3]
    nodes = []
    
    for i, num in enumerate(vals):
        node = ListNode(num, None)
        if i > 0:
            nodes[-1].next = node
        nodes.append(node)

    solution.reverseList(nodes[0])


    for node in reversed(nodes[]):
        print(node.val, node.next.val)
