class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s :
            return 0
        l,r=0,1
        count=1
        charset=set()
        charset.add(s[l])
        maxcount=1
        while r <len(s):
            if s[r] not in charset:
                charset.add(s[r])
                count+=1
                maxcount=max(count,maxcount)
            else:
                
                l = r                      # ✅ reset left pointer
                count = 1
                charset.clear()            # ✅ clear set instead of removing
                charset.add(s[r])    
            r+=1
        return maxcount


        


            