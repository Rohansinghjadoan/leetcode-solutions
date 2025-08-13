class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count={}
        frq=[[] for i in range(len(nums)+1)]
        for num in nums:
            count[num]=1+count.get(num,0)
        for num ,cnt in count.items():
            frq[cnt].append(num)
        res=[]
        for i in range(len(frq)-1,0,-1):
            for num in frq[i]:
                res.append(num)
                if len(res)==k:
                    return res
                    
       