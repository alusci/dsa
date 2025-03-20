# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/description/?


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        if k > len(blocks):
            return 0

        p1 = 0
        p2 = k - 1

        white_counts = 0
        black_counts = 0

        p = 0
        while p <= p2:
            if blocks[p] == "W":
                white_counts += 1
            else:
                black_counts += 1

            p += 1

        min_recolors = 0
        if black_counts < k:
            min_recolors = white_counts
        else:
            min_recolors = 0

        while p2 < len(blocks) - 1:

            if blocks[p1] == "W":
                white_counts -= 1
            else:
                black_counts -= 1

            p1 += 1
            p2 += 1

            if blocks[p2] == "W":
                white_counts += 1
            else:
                black_counts += 1

            if black_counts < k:
                min_recolors = min(min_recolors, white_counts)
            else:
                min_recolors = 0

        return min_recolors
