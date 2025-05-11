class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for num in range(len(nums)):
            if nums[num]==target:
                res.append(num)
        return res