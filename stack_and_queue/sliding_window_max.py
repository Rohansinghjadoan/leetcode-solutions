
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q=deque()
        r=[]
        n=len(nums)
        for i in range(n):
            if q and q[0]==i-k:

                q.popleft()
            while q and nums[q[-1]]<nums[i]:
                q.pop() ## pop back
            q.append(i)
            if i>=k-1:
                r.append(nums[q[0]])
        return r