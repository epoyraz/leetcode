class Solution:
    def secondGreaterElement(self, nums):
        n = len(nums)
        ans = [-1] * n
        stack1 = []  # indices waiting for their first greater
        stack2 = []  # indices waiting for their second greater

        for i, x in enumerate(nums):
            # First, resolve any second-greater for stack2
            while stack2 and x > nums[stack2[-1]]:
                idx = stack2.pop()
                ans[idx] = x

            # Next, move from stack1 to stack2 when we find first greater
            temp = []
            while stack1 and x > nums[stack1[-1]]:
                temp.append(stack1.pop())
            # Those popped now await their second greater
            stack2.extend(reversed(temp))

            # Finally, this index itself awaits its first greater
            stack1.append(i)

        return ans
