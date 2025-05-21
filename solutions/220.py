class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0:
            return False

        width = valueDiff + 1  # bucket size
        bucket = {}

        for i, num in enumerate(nums):
            bucket_id = num // width

            if bucket_id in bucket:
                return True
            if bucket_id - 1 in bucket and abs(num - bucket[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in bucket and abs(num - bucket[bucket_id + 1]) <= valueDiff:
                return True

            bucket[bucket_id] = num

            if i >= indexDiff:
                old_bucket_id = nums[i - indexDiff] // width
                del bucket[old_bucket_id]

        return False
