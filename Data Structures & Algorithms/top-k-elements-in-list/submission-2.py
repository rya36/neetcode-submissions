class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track = {}
        res = []

        for n in nums:
            track[n] = track.get(n, 0) + 1
        
        res = sorted(track, key=track.get)

        return res[-k:]