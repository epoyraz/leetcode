class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow, fast = i, next_index(i)
            while nums[slow] * nums[fast] > 0 and nums[slow] * nums[next_index(fast)] > 0:
                if slow == fast:
                    if slow == next_index(slow):
                        break
                    return True
                slow = next_index(slow)
                fast = next_index(next_index(fast))

            # mark the path as visited
            j = i
            while nums[j] * nums[next_index(j)] > 0:
                temp = j
                j = next_index(j)
                nums[temp] = 0

        return False
