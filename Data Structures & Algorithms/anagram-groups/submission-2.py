class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}

        for i in range(len(strs)):
            x = {}
            for char in strs[i]:
                x[char] = x.get(char, 0) + 1
            key = tuple(sorted(x.items()))
            result[key] = result.get(key, [])
            result[key].append(strs[i])
        
        return list(result.values())
            
        
        
        