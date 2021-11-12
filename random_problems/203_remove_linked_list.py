# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev= None 
        pointer = head
        
        while pointer:
            if pointer.val == val:  
                if prev: 
                    prev.next = pointer.next
                else: 
                    head = pointer.next
                pointer = pointer.next 
            else:  
                prev, pointer = pointer, pointer.next
        return head
        