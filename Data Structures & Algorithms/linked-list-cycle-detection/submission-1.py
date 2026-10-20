# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
# two pointers, one moves two steps at a time, if the faster one catches up, there is a cycle, otherwise if fast reaches a null, there is no cycle
        if head is None or head.next is None:
            return False

        fast = head.next.next
        slow = head

        while fast != slow:
            if fast is None or fast.next is None:
                return False
            else:
                fast = fast.next.next
                slow = slow.next
        return True