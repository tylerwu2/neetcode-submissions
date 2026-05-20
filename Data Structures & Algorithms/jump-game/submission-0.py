class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # IDEA: top-down approach start from back or array and move forwards if can reach target 

        # dp = [0 for num in nums]

        # for i in range(len(nums) -1, -1, -1):
        #     if i == len(nums) - 1:
        #         dp[len(nums) - 1] = True 
        #     else:
        #         dp[i] = sum([dp[j] for j in range(i + dp[i] + 1)]) >= 1

        # return dp[0] 

        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= target:
                target = i
        
        return target == 0