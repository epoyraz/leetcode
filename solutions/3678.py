import heapq

class TaskManager(object):
    def __init__(self, tasks):
        """
        :type tasks: List[List[int]]   # each [userId, taskId, priority]
        """
        # info: taskId -> (userId, priority)
        self.info = {}
        # max-heap storing (-priority, -taskId, taskId)
        self.heap = []
        
        for userId, taskId, priority in tasks:
            self.info[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def add(self, userId, taskId, priority):
        """
        :type userId: int
        :type taskId: int
        :type priority: int
        :rtype: None
        """
        # insert new task
        self.info[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, taskId))

    def edit(self, taskId, newPriority):
        """
        :type taskId: int
        :type newPriority: int
        :rtype: None
        """
        userId, _old = self.info[taskId]
        # update mapping
        self.info[taskId] = (userId, newPriority)
        # push updated entry
        heapq.heappush(self.heap, (-newPriority, -taskId, taskId))

    def rmv(self, taskId):
        """
        :type taskId: int
        :rtype: None
        """
        # lazy-delete by removing from info
        if taskId in self.info:
            del self.info[taskId]

    def execTop(self):
        """
        :rtype: int  # userId of executed task, or -1 if none
        """
        # pop until we find a valid top
        while self.heap:
            neg_prio, neg_tid, tid = heapq.heappop(self.heap)
            prio, tid_pos = -neg_prio, -neg_tid
            # check consistency with current info
            if tid_pos in self.info:
                userId, cur_prio = self.info[tid_pos]
                if cur_prio == prio:
                    # this is the true top; execute it
                    del self.info[tid_pos]
                    return userId
            # otherwise it's staleâkeep popping
        return -1
