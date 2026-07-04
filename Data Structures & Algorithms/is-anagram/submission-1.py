class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        dictS = {}
        dictT = {}

        for i in s:
            dictS[i] = dictS.get(i, 0) + 1

        for i in t:
            dictT[i] = dictT.get(i, 0) + 1
        
        return dictS == dictT
        
