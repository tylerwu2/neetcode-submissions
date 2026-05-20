class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #IDEA: similar to two sum, but fix first position and set left and right pointers to the right of the array

        nums = sorted(nums)
        output = []

        for i in range(len(nums)):
            first = nums[i]
            l, r = i + 1, len(nums) - 1
            
            # break loop when triplet is found
            while l < r:
                if first + nums[l] + nums[r] > 0: 
                    r -= 1
                elif first + nums[l] + nums[r] < 0:
                    l += 1
                elif (first + nums[l] + nums[r]) == 0: 
                    if [first, nums[l], nums[r]] not in output:
                        output.append([first, nums[l], nums[r]])
                    l += 1
                
        return output 
