class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for num in nums] 

        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-1] + nums[i], nums[i])

        return max(dp)