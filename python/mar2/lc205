class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        rep = {}
        for a, b in zip(s, t):
            if a in rep.keys() and rep[a] != b:
                return False
            elif a not in rep.keys() and b in rep.values():
                return False
            else:
                rep[a] = b
               
        return True
