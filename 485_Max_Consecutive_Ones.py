class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_count=0
        for i in nums:
            if i==1:
                count = count+1
                if max_count<count:
                    max_count=count
            else:
                count=0
        return max_count
