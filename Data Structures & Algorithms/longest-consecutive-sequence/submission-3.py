class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        s = set(nums)
        count = 1
        maxCount = 1
        for n in s:
            if n - 1 not in s:
                i = n + 1
                while i in s:
                    count += 1
                    i += 1
                maxCount = max(count, maxCount)
                count = 1
        return maxCount
