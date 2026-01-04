# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        groupPrev=ListNode(0,head)
        dummy=groupPrev

        while True:
            kth=self.getKth(groupPrev, k)
            if not kth:
                break        
            groupNext=kth.next
            prev, curr=kth.next,groupPrev.next
            while curr!=groupNext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp

            tmp=groupPrev.next #1st element
            groupPrev.next=kth #since reversed, kth element is 1st now
            groupPrev=tmp #setting the 1st element as groupPrev for next grp
        return dummy.next
                 
    def getKth(self, curr,k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr