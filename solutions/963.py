class Solution:
    def threeEqualParts(self, arr):
        total = sum(arr)
        n = len(arr)

        if total == 0:
            return [0, n - 1]  # all zeroes

        if total % 3 != 0:
            return [-1, -1]

        k = total // 3
        first = second = third = -1
        count = 0

        # Find starting indices of each part
        for i, val in enumerate(arr):
            if val == 1:
                count += 1
                if count == 1:
                    first = i
                elif count == k + 1:
                    second = i
                elif count == 2 * k + 1:
                    third = i

        # Compare the parts
        while third < n:
            if arr[first] != arr[second] or arr[second] != arr[third]:
                return [-1, -1]
            first += 1
            second += 1
            third += 1

        return [first - 1, second]
