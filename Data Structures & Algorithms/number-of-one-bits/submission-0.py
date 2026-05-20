class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0
        for i in range(32):
            bitmask = 1 << i
            if n & bitmask > 0:
                ones += 1
        
        return ones
