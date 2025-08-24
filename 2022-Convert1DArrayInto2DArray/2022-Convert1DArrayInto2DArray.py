# Last updated: 8/24/2025, 12:39:08 AM
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        
        ele = 0
        result = []
        
        for i in range(m):
            row = []
            for j in range(n):
                row.append(original[ele])
                ele += 1
            result.append(row)
        
        return result


