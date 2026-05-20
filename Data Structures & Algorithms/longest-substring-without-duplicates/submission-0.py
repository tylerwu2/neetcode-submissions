class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        character_set = set()

        l = 0
        res = 0

        for i in range(len(s)):
            while s[i] in character_set:
                character_set.remove(s[l])
                l += 1
            character_set.add(s[i])
            res = max(res, i - l + 1)
        return res