class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagrams = [] 

        # str_dicts = [] 

        # if len(strs) == 1:
        #     return [strs]
        # else:
        #     for str in strs: 
        #         str_dict = {}
        #         for letter in str: 
        #             if letter in str_dict:
        #                 str_dict[letter] += 1
        #             else:
        #                 str_dict[letter] = 1
                
        #         if str_dict not in str_dicts:
        #             str_dicts.append(str_dict)
        #         anagrams.append(str)
                

        anagrams = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())