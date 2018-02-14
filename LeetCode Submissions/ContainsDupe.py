'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.


'''
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import defaultdict
        d = defaultdict(int)
        for x in nums:
            d[x] +=1
            
        for x in d.values():
            if x > 1:
                return True
        
        return False
        