class Solution:
    def mostPopularCreator(self, creators, ids, views):
        # Track per-creator data:
        # popularity[c] = total views
        # best_video[c] = (max_views, lex_smallest_id)
        popularity = {}
        best_video = {}
        
        for c, vid, v in zip(creators, ids, views):
            # Update total popularity
            popularity[c] = popularity.get(c, 0) + v
            
            # Update this creator's best video
            if c not in best_video:
                best_video[c] = (v, vid)
            else:
                mv, mid = best_video[c]
                if v > mv or (v == mv and vid < mid):
                    best_video[c] = (v, vid)
        
        # Find maximum popularity
        max_pop = max(popularity.values())
        
        # Collect all creators at that popularity
        ans = []
        for c, pop in popularity.items():
            if pop == max_pop:
                _, vid = best_video[c]
                ans.append([c, vid])
        
        return ans
