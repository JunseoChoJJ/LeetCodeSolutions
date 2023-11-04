# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cnt = 0
        curr = head
        while curr:
            cnt += 1
            curr = curr.next
        print(cnt)
        count = cnt - n - 1
        
        if count < 0:
            return head.next
        check = 0
        list1 = head
        print(count)
        while list1:
            
            if check == count:
                list1.next = list1.next.next
                break
            check += 1    
            list1 = list1.next
        return head
            

        '''
        # two pointeer explanation 
        list1 = head
        list2 = head
        for i in range(n):
            list1 = list1.next
        if not list1:
            return head.next

        while list1.next:
            list2 = list2.next
            list1 = list1.next
        list2.next = list2.next.next
        
        return head
        '''
