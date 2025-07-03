class Solution(object):
    def rob(self, nums):
        a=b=0
        for n in nums:
            a,b=b,max(a+n, b)
        return b
        