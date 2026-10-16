class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 1
        curr_max = max(nums[0:k])
        window_max = [curr_max]
        while left + k - 1 < len(nums):
            print(left)
            if nums[left + k - 1] > curr_max:
                curr_max = nums[left + k - 1]
            elif nums[left - 1] == curr_max:
                curr_max = max(nums[left:left+k])
            window_max.append(curr_max)
            left += 1
        return window_max