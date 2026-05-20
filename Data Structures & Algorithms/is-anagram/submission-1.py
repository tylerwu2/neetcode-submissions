class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]] += 1
            else:
                s_dict[s[i]] = 1

        for j in range(len(t)):
            if t[j] in t_dict:
                t_dict[t[j]] += 1
            else:
                t_dict[t[j]] = 1

        for key in s_dict.keys():
            if key in s_dict and key in t_dict:
                if s_dict[key] != t_dict[key]:
                    return False
                continue
            return False

        return True 