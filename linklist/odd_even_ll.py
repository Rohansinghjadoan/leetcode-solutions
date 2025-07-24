class Solution(object):
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        evenhead = even  # to connect at the end

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenhead
        return head
