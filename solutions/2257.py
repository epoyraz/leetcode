class Solution:
    def earliestFullBloom(self, plantTime, growTime):
        seeds = sorted(zip(growTime, plantTime), reverse=True)
        curr_day = 0
        max_bloom = 0
        for g, p in seeds:
            curr_day += p
            max_bloom = max(max_bloom, curr_day + g)
        return max_bloom
