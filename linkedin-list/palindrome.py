from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
 
class Solution:
    def halfLinkedList(self, head: Optional[ListNode]) -> ListNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseLinkedinList(self, head):
        prev = None
        cur = head
        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        half = self.halfLinkedList(head)
        rev = self.reverseLinkedinList(half)

        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        
        return True
        