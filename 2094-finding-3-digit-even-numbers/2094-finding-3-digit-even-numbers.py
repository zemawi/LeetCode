from typing import List
from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()
        
        for perm in permutations(digits, 3):
            # Skip leading zero
            if perm[0] == 0:
                continue
            
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            # Check if number is even
            if num % 2 == 0:
                result.add(num)
        
        return sorted(result)
