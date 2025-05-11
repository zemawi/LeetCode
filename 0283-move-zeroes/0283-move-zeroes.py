class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[f] , nums[i] =nums[i] , nums[f]
                f += 1
        return nums
        