class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            nums_map[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums_map and nums_map[diff] != i:
                return [i, nums_map[diff]]
