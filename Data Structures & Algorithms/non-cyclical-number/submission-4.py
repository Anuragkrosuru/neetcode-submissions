class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()

        while n != 1:
            if n in set1:
                return False
            set1.add(n)

            result = 0
            for digit in str(n):
                result += int(digit) ** 2 
            n = result


        return True