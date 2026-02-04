# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        node = head

        while node:

            next = node.next # 1.다음 노드값 저장
            node.next = prev # 2.현재 노드값의 방향을 반대로 돌림.
            prev = node # 3.prev를 현재로 이동
            node = next # 4.curr을 다음으로 이동

        return prev
        