class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # top-down approach, build from last temp to first, looking for decreasing subseq
        warmer_temp = [0 for i in range(len(temperatures))]
        
        #base case for last element
        warmer_temp[len(temperatures) - 1] = 0

        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1

            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if warmer_temp[j] == 0:
                    j = len(temperatures)
                    break
                j += warmer_temp[j] 
            
            if j < len(temperatures):
                warmer_temp[i] = j - i

            
        return warmer_temp