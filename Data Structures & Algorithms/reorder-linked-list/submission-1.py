# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        right = slow.next
        slow.next = None
  
        while right:
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp

        left = head
        right = prev

        while right:
            tmp1 = left.next
            tmp2 = right.next
            left.next = right
            right.next = tmp1
            left = tmp1
            right = tmp2

    




'''
          [p]
[0, 1, 2, 3, 4, 5, 6]
[         s.        ]


[0, 1, 2, 3] [6, 5, 4]
'''