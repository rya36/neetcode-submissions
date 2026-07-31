class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        paths = []
        used = set()

        def dfs():

            if len(paths) == len(nums):
                res.append(paths[:])
                return

            for num in nums:
                if num in used:
                    continue
                paths.append(num)
                used.add(num)
                dfs()
                paths.pop()
                used.remove(num)
        
        dfs()
        return res