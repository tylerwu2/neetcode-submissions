class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        product = nums[0]
        curr_max = 1
        curr_min = 1

        for num in nums:
            tmp = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(tmp, num * curr_min, num)
            product = max(product, curr_max)

        return product