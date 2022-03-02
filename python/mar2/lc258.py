class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        else:
            mod = num % 9
            if mod:
                return mod
            else:
                return 9
      
