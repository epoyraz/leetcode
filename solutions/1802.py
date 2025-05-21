class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # Count how many students prefer each type
        count0 = students.count(0)
        count1 = len(students) - count0
        
        # Serve sandwiches in order
        for s in sandwiches:
            if s == 0:
                if count0 > 0:
                    count0 -= 1
                else:
                    break
            else:  # s == 1
                if count1 > 0:
                    count1 -= 1
                else:
                    break
        
        # Remaining students unable to eat
        return count0 + count1
