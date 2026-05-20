class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # first sort the hand O(nlogn)
        hand.sort()  
        freq_map = {}
        
        # construct frequency map 
        for i in range(len(hand)):
            freq_map[hand[i]] = freq_map.get(hand[i], 0) + 1

        for i in range(len(hand)): 
            if freq_map[hand[i]]:
                for j in range(hand[i], hand[i] + groupSize):
                    if j not in freq_map or freq_map[j] == 0:
                        return False
                    freq_map[j] -= 1
        return True 
