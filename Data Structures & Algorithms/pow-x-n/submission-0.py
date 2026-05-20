class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        answer = 1
        power = abs(n)

        while power:
            if power % 2 == 1:
                answer *= x
            x *= x
            power >>= 1
        
        if n >= 0:
            return answer
        else:
            return 1 / answer


        