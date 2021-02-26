class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        token = 0
        for i in nums:
            temp = i**2
            nums[token] = temp
            token += 1
        nums = sorted(nums, reverse=False)
        return nums
        # return sorted(x*x for x in nums)
