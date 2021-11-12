# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        fo=None
        f_ptr = fo
        while(l1 != None and l2 != None ):
            if l1.val <= l2.val :
                temp = ListNode(l1.val, None)
                l1 = l1.next
            else : 
                temp = ListNode(l2.val)
                l2 = l2.next      
            if f_ptr == None:
                f_ptr = temp
                fo = f_ptr
            else:
                f_ptr.next = temp
                f_ptr = f_ptr.next
                
        while(l1 != None ): 
            if f_ptr == None:
                f_ptr = ListNode(l1.val, None)
                fo = f_ptr
            else:
                f_ptr.next = ListNode(l1.val)
                f_ptr = f_ptr.next
            l1 = l1.next   
            
        while(l2 != None ): 
            if f_ptr == None:
                f_ptr = ListNode(l2.val, None)
                fo = f_ptr
            else:
                f_ptr.next = ListNode(l2.val) 
                f_ptr = f_ptr.next
            l2 = l2.next
            
        return fo