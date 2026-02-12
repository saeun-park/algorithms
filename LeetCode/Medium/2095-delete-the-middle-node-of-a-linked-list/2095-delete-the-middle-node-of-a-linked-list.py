# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        
        if not head.next:
            return None
        
        while node:
            length += 1
            node = node.next
        middle = length // 2
        
        prev = head
        for _ in range(middle-1): # ex1을 예시로 들었을 때, 2번 반복하게 되어 1->3->4만 살게 된다.
            prev = prev.next
        
        prev.next = prev.next.next

        return head

