class Solution:
    def oddEvenJumps(self, arr):
        n = len(arr)
        next_higher = [0] * n
        next_lower = [0] * n

        def make_monotonic_stack(indexes):
            result = [0] * n
            stack = []
            for i in indexes:
                while stack and i > stack[-1]:
                    result[stack.pop()] = i
                stack.append(i)
            return result

        # Prepare indices sorted for odd (ascending value) and even (descending value) jumps
        sorted_higher = sorted(range(n), key=lambda i: (arr[i], i))
        sorted_lower = sorted(range(n), key=lambda i: (-arr[i], i))

        next_higher = make_monotonic_stack(sorted_higher)
        next_lower = make_monotonic_stack(sorted_lower)

        odd = [False] * n
        even = [False] * n
        odd[-1] = even[-1] = True

        for i in range(n - 2, -1, -1):
            if next_higher[i]:
                odd[i] = even[next_higher[i]]
            if next_lower[i]:
                even[i] = odd[next_lower[i]]

        return sum(odd)
