class Solution(object):
    def hardestWorker(self, n, logs):
        max_time = -1
        worker_id = None
        prev_end = 0

        for emp_id, leave in logs:
            duration = leave - prev_end
            if duration > max_time or (duration == max_time and emp_id < worker_id):
                max_time = duration
                worker_id = emp_id
            prev_end = leave

        return worker_id
