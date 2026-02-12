# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        end = len(arr)-1
        start = 0
        maxsum = 0
        while start < end:
            maxsum = max(maxsum, arr[start]+arr[end])
            start += 1
            end-= 1
        return maxsum
