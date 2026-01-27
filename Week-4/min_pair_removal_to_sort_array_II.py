import heapq

class Solution:
    def minimumPairRemoval(self, nums):
        n = len(nums)

        # temp as long long equivalent
        temp = [int(x) for x in nums]

        # doubly linked list via arrays
        nextIndex = [i + 1 for i in range(n)]
        prevIndex = [i - 1 for i in range(n)]

        # min heap for (pair_sum, index)
        heap = []

        # to validate heap entries (lazy deletion)
        valid = {}

        badPairs = 0

        # initialize badPairs + heap
        for i in range(n - 1):
            if temp[i] > temp[i + 1]:
                badPairs += 1
            pair_sum = temp[i] + temp[i + 1]
            heapq.heappush(heap, (pair_sum, i))
            valid[(i, pair_sum)] = True

        operations = 0

        while badPairs > 0:
            # extract valid min pair
            while heap:
                pair_sum, first = heap[0]
                if valid.get((first, pair_sum), False) and nextIndex[first] < n:
                    break
                heapq.heappop(heap)

            pair_sum, first = heapq.heappop(heap)
            valid[(first, pair_sum)] = False

            second = nextIndex[first]
            first_left = prevIndex[first]
            second_right = nextIndex[second]

            # remove bad pair (first, second)
            if temp[first] > temp[second]:
                badPairs -= 1

            # {d, (a, b)}
            if first_left >= 0:
                if temp[first_left] > temp[first] and temp[first_left] <= temp[first] + temp[second]:
                    badPairs -= 1
                elif temp[first_left] <= temp[first] and temp[first_left] > temp[first] + temp[second]:
                    badPairs += 1

            # {(a, b), d}
            if second_right < n:
                if temp[second_right] >= temp[second] and temp[second_right] < temp[first] + temp[second]:
                    badPairs += 1
                elif temp[second_right] < temp[second] and temp[second_right] >= temp[first] + temp[second]:
                    badPairs -= 1

            # update heap pairs around merged node
            # left neighbor: (first_left, first)
            if first_left >= 0:
                old_sum = temp[first_left] + temp[first]
                valid[(first_left, old_sum)] = False

                new_sum = temp[first_left] + temp[first] + temp[second]
                heapq.heappush(heap, (new_sum, first_left))
                valid[(first_left, new_sum)] = True

            # right neighbor: (second, second_right) removed, new pair (first, second_right)
            if second_right < n:
                old_sum = temp[second] + temp[second_right]
                valid[(second, old_sum)] = False

                new_sum = temp[first] + temp[second] + temp[second_right]
                heapq.heappush(heap, (new_sum, first))
                valid[(first, new_sum)] = True

                prevIndex[second_right] = first

            # merge second into first
            nextIndex[first] = second_right
            temp[first] += temp[second]

            operations += 1

        return operations
