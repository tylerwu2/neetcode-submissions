class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # IDEA: left and right pointers and keep track of maximum 

        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r:
            # maxArea = maxHeight * distance between containers
            max_height = min(heights[l] , heights[r])
            dist = r - l
            max_area = max(max_area, max_height * dist)

            # how to move pointers?
            if heights[l] == max_height:
                l += 1
            else:
                r -= 1
        
        return max_area 