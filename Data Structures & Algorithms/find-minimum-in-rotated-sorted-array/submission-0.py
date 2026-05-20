class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find where both values are less than the current value
        l, r = 0, len(nums) - 1

        while l < r: 
            mid = (l + (r - 1)) // 2 
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        
        return nums[l]
                