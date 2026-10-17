class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # deque solution
        # keep track of possible candidaes for max
        # O(k) space, O(n) worst case

        candidates = deque() 
        window_max = []
        left, right = 0, 0

        while right < len(nums):
            while candidates and nums[candidates[-1]] < nums[right]:
                candidates.pop()
            candidates.append(right)

            if left > candidates[0]:
                candidates.popleft()

            if (right + 1) >= k:
                window_max.append(nums[candidates[0]])
                left += 1
            right += 1
        return window_max