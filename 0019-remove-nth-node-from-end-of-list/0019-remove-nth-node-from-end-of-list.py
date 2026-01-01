# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        new_curr=prev
        before=None
        p=0
        while new_curr:
            p+=1           
            if p==n:
                if n==1:
                    prev=prev.next
                    break       
                before.next=before.next.next
            before=new_curr
            new_curr=new_curr.next

        final_head=prev
        bef=None
        while prev:
            t=prev.next
            prev.next=bef
            bef=prev
            prev=t

        return bef


        