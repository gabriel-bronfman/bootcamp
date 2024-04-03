class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        people = [0] * forget
        people[0] = 1
        
        for i in range(1, n):
            for idx in range(forget - 1, 0, -1):
                people[idx] = people[idx - 1] 
            
            new = 0
            for idx in range(forget):
                if idx >= delay:
                    new = (new + people[idx])%1000000007
                    
            people[0] = new
            
        total = 0
        for p in people:
            total = (total + p)%1000000007
            
        return total     