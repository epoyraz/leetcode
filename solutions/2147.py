class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        def evaluate(expr):
            nums = []
            i = 0
            while i < len(expr):
                if expr[i].isdigit():
                    nums.append(int(expr[i]))
                elif expr[i] == '*':
                    a = nums.pop()
                    b = int(expr[i + 1])
                    nums.append(a * b)
                    i += 1
                elif expr[i] == '+':
                    nums.append('+')
                i += 1
            res = nums[0]
            i = 1
            while i < len(nums):
                if nums[i] == '+':
                    res += nums[i + 1]
                    i += 2
                else:
                    i += 1
            return res

        # Tokenize
        tokens = []
        for ch in s:
            if ch.isdigit():
                tokens.append(int(ch))
            else:
                tokens.append(ch)

        memo = {}

        def dfs(l, r):
            key = (l, r)
            if key in memo:
                return memo[key]
            if l == r:
                return set([tokens[l]])
            results = set()
            for i in range(l + 1, r, 2):
                op = tokens[i]
                left = dfs(l, i - 1)
                right = dfs(i + 1, r)
                for a in left:
                    for b in right:
                        if op == '+':
                            val = a + b
                        else:
                            val = a * b
                        if 0 <= val <= 1000:
                            results.add(val)
            memo[key] = results
            return results

        correct = evaluate(s)
        wrong_set = dfs(0, len(tokens) - 1)
        if correct in wrong_set:
            wrong_set.remove(correct)

        score = 0
        for ans in answers:
            if ans == correct:
                score += 5
            elif ans in wrong_set:
                score += 2
        return score
