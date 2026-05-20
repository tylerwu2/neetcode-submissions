class Solution:
    def rob(self, nums: List[int]) -> int:
        ## goal: maximize the amount of money at house i, compare between either selecting current house or not

        dp = [0 for _ in range(len(nums))]
        ## BASE CASE:
        if len(nums) <= 2:
            return max(nums)
        else:
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1]) 
        print(dp)
        return dp[len(nums) - 1]