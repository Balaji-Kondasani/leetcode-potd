class Solution(object):
    def maximizeSquareArea(self, m, n, hFences, vFences):
        
        MOD = 1000000007

        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)

        hFences.sort()
        vFences.sort()

        widths = set()
        for i in range(len(vFences)):
            for j in range(i + 1, len(vFences)):
                widths.add(vFences[j] - vFences[i])

        max_area = -1
        for i in range(len(hFences)):
            for j in range(i + 1, len(hFences)):
                side = hFences[j] - hFences[i]
                if side in widths:
                    max_area = max(max_area, side * side)

        return max_area % MOD if max_area != -1 else -1


