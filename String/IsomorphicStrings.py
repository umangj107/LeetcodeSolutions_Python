class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s = {}
        mapping_t = {}
        
        for i,j in zip(s,t):
            if i not in mapping_s and j not in mapping_t:
                mapping_s[i] = j
                mapping_t[j] = i
                
            elif mapping_s .get(i) != j or mapping_t.get(j) != i:
                return False
            
        return True
