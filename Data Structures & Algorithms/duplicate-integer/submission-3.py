class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = {}

        for n in nums:
            track[n] = track.get(n, 0) + 1
        
        for n in nums:
            if track[n] > 1:
                return True
        return False
        