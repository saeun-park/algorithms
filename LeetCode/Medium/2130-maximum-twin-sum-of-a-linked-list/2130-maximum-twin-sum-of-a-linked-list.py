class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        front = head
        back = prev
        maxsum = 0
        while back:
            maxsum = max(maxsum, front.val + back.val)
            front = front.next
            back = back.next
        return maxsum

