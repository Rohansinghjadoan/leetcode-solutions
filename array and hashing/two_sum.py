class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        prevmap={}
        index=0
        for i in nums:
            diff= target-i
            if diff in prevmap:
                return[prevmap[diff],index]
            prevmap[i]=index
            index+=1


