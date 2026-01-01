# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #O(n), O(1):time,space
        # slow,fast=head,head.next
        # while(fast and fast.next):
        #     slow=slow.next
        #     fast=fast.next.next

        # second=slow.next #beginning of second list
        # slow.next=None
        # prev=None
        # #Reversing second list
        # while second:
        #     temp=second.next
        #     second.next=prev
        #     prev=second
        #     second=temp

        # first, second=head, prev
        # while second:
        #     tmp1, tmp2=first.next, second.next
        #     first.next=second
        #     second.next=tmp1
        #     first=tmp1
        #     second=tmp2

        curr=head
        arr=[]
        while curr:
            arr.append(curr)
            curr=curr.next
        
        i, j=0, len(arr)-1
        while i<j:
            arr[i].next=arr[j]
            i+=1
            if i>=j:
                break
            arr[j].next=arr[i]
            j-=1
            
        arr[i].next=None







        
        
        