class Solution(object):
    def calculateScore(self, instructions, values):
        """
        :type instructions: List[str]
        :type values: List[int]
        :rtype: int
        """
        n = len(instructions)
        visited = set()
        score = 0
        i = 0

        while 0 <= i < n and i not in visited:
            visited.add(i)
            instr = instructions[i]
            val = values[i]

            if instr == "add":
                score += val
                i += 1
            else:  # "jump"
                i += val

        return score
