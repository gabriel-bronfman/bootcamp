class Solution:
     def videoStitching(self, clips, T):
        left, right, count = -1, 0, 0
        for i, j in sorted(clips):
            if right >= T or i > right:
                break
            elif left < i <= right:
                count, left = count + 1, right
            right = max(right, j)
        return count if right >= T else -1