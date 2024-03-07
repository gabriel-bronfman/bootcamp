class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charDict = {}
        res = 0
        most = 0
        l = 0

        for r,char in enumerate(s):
            
            
            if char in charDict:
                charDict[char] += 1
            else:
                charDict[char] = 1

            most = max(most, charDict[char])

            if r - l + 1 - most > k:
                charDict[s[l]] -= 1
                l += 1

            res = max(res, r-l+1)
        return res
