# Last updated: 8/23/2025, 5:12:27 AM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap = {}
        
        for si in s:
            hmap[si] = hmap.get(si, 0) + 1
        
        for ti in t:
            if ti not in hmap or hmap[ti] == 0:
                return False 
            
            hmap[ti] -= 1
            if hmap[ti] == 0:
                del hmap[ti]

        if len(hmap.keys()) != 0:
            return False 
            
        return True


        