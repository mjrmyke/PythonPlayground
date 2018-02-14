'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        for x in nums:
            d[x] +=1
        
        for k,v in d.iteritems():
            if v == 1:
                return k
            