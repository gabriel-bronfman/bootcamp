class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        i, num, sign = 0, 0, 1

        if s[0] == "+" or s[0] == "-":
            sign = 1 if s[0] == "+" else -1
            i += 1
        
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            num = num * 10 + digit
            i += 1
        
        if num > (2**31)-1:
            if sign < 0:
                num = 2**31
            else:
                num = 2**31 - 1
        
        
        return num * (sign) 