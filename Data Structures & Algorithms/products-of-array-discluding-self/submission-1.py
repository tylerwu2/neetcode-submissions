class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ## IDEA: find total product of array except 0s
        total_product = 1
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                total_product *= nums[i]
            else: 
                zeroes += 1

        output = []
        
        if zeroes > 1:
            output = [0 for _ in range(len(nums))]
            return output

        for j in range(len(nums)):
            # edge case where there is one 0 
            if nums[j] == 0:
                output = [0 for _ in range(len(nums))]
                output[j] = total_product 
                break 
            else:
                output.append(int(total_product/nums[j]))

        return output