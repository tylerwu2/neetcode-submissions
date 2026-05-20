class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # IDEA: sliding window where 1st letter and last letter must be part of the target string (minimizes length of substring) 

        # iterate through entire string, if t is not empty, return empty string, otherwise return substring

        if t == "":
            return ""
        
        t_freq = {}
        window = {}

        # generates frequency map for target string         
        # dict.get(c, 0), access dictionary value for c, default value of 0 if it doesn't exist yet 
        for char in t:
            t_freq[char] = 1 + t_freq.get(char, 0)

        match = 0
        need = len(t_freq)

        res = [-1, -1]
        res_len = float("infinity")

        # initializes left pointer to start of string
        l = 0

        # iterate over right pointers
        for r in range(len(s)):
            char = s[r]
            window[char] = 1 + window.get(char, 0)

            if char in t_freq and window[char] == t_freq[char]:
                match += 1

            while match == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in t_freq and window[s[l]] < t_freq[s[l]]:
                    match -= 1
                l += 1
        l, r = res

        if res_len != float("infinity"):
            return s[l : r + 1]
        else:
            return ""