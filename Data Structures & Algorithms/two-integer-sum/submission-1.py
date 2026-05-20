class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i in range(len(nums)):
            num_dict[nums[i]] = i 

        for i in range(len(nums)): 
            diff = target - nums[i] 
            if diff in num_dict and num_dict[diff] != i: 
                return [i, num_dict[diff]]