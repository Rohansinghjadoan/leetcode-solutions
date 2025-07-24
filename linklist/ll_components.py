# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: Optional[ListNode]
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        current = head
        count = 0

        while current:
            if current.val in num_set and (not current.next or current.next.val not in num_set):
                count += 1
            current = current.next
        return count       