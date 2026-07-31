class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        paths = []

        def dfs(start):
            res.append(paths[:])

            for i in range(start, len(nums)):
                paths.append(nums[i])
                dfs(i + 1)
                paths.pop()
            
        dfs(0)

        return res
