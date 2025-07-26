class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nge = {}
        st = []

        # Step 1: Process nums2 using stack to get next greater for every element
        for num in nums2:
            while st and st[-1] < num:
                smaller = st.pop()
                nge[smaller] = num
            st.append(num)

        # Step 2: For any remaining elements, no next greater exists
        while st:
            nge[st.pop()] = -1

        # Step 3: Prepare answer for nums1 using precomputed nge
        return [nge[num] for num in nums1]
