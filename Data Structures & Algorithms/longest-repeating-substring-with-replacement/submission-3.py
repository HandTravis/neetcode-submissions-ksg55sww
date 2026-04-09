class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        counts = [0] * 26
        left = 0
        max_count = 0
        best = 0

        for right in range(n):
            idx = ord(s[right]) - ord('A')
            counts[idx] += 1
            max_count = max(max_count, counts[idx])

            while (right - left + 1) - max_count > k:
                left_idx = ord(s[left]) - ord('A')
                counts[left_idx] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


