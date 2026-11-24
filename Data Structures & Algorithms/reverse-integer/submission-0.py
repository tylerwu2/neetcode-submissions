class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = False
        else:
            sign = True

        x = abs(x)
        reverse_x = 0
        while x != 0:
            dig = x % 10
            reverse_x = reverse_x * 10 + dig
            print(reverse_x)
            if (reverse_x < (-2 ** 31) or reverse_x > (2 ** 31 - 1)):
                return 0 
            x //= 10


        if sign:
            return reverse_x
        else:
            return - reverse_x