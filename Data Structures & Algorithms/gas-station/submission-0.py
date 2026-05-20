class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # IDEA: sum over total cost, if difference between gas used and gas gained is too much discard solution 
        if sum(gas) < sum(cost):
            return -1

        total = 0
        response = 0

        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                response = i + 1
        
        return response