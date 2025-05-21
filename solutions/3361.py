class Solution(object):
    def findLatestTime(self, s):
        """
        :type s: str
        :rtype: str
        """
        # convert to list for mutability
        t = list(s)
        
        # Hour tens (t[0])
        if t[0] == '?':
            # If hour ones is '?' or <= '1', we can pick '1'; else must pick '0'
            if t[1] == '?' or t[1] <= '1':
                t[0] = '1'
            else:
                t[0] = '0'
        
        # Hour ones (t[1])
        if t[1] == '?':
            # If tens is '0', ones can be '9'; if tens is '1', ones max is '1'
            if t[0] == '0':
                t[1] = '9'
            else:  # t[0] == '1'
                t[1] = '1'
        
        # Minute tens (t[3])
        if t[3] == '?':
            t[3] = '5'
        
        # Minute ones (t[4])
        if t[4] == '?':
            t[4] = '9'
        
        return "".join(t)
