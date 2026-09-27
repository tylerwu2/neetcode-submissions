class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob_linear(nums):
            prev2 = 0
            prev1 = 0

            for num in nums:
                curr = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = curr

            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(
            rob_linear(nums[:-1]),
            rob_linear(nums[1:])
        )