class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## iterate throught list of numbers 
        ## keep track of only 1 number
        XOR = nums[0]

        for i in range(1, len(nums)):
            XOR = XOR ^ nums[i]
            
        return XOR
        