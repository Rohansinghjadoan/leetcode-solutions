# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        # Step 1: Find middle using fast/slow
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Reverse second half
        second_half = self.reverse(slow.next)
        first_half = head
        temp = second_half  # for restoring later if needed

        # Step 3: Compare both halves
        while second_half:
            if first_half.val != second_half.val:
                self.reverse(temp)  # optional: restore list
                return False
            first_half = first_half.next
            second_half = second_half.next

        # Step 4: Restore list (optional)
        self.reverse(temp)
        return True

    # Helper function to reverse a linked list
    def reverse(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
