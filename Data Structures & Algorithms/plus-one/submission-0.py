class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] + 1 != 10: 
            digits[-1] = digits[-1] + 1
            return digits
        else:
            # case when new_digit = 10
            carry = 1
            new_digit = digits[-1] + 1
            digits[-1] = 0
            for i in range(len(digits) - 2, -1, -1):
                new_digit = digits[i] + carry
                if new_digit >= 10:
                    carry = 1
                    digits[i] = new_digit % 10
                else:
                    digits[i] = new_digit
                    carry = 0
                
            if carry == 1:
                digits = [1] + digits

            return digits