class Solution(object):
    def convertTime(self, current, correct):
        ch, cm = map(int, current.split(':'))
        uh, um = map(int, correct.split(':'))
        diff = (uh * 60 + um) - (ch * 60 + cm)
        ops = 0
        for step in (60, 15, 5, 1):
            ops += diff // step
            diff %= step
        return ops
