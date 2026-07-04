class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}

        for i, num in enumerate(nums):
            track[num] = i
        
        for i, n in enumerate(nums):
            if target - n in track and track[target - n] != i:
                return [i, track[target - n]]

        return []

        