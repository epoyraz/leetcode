class Solution:
    def minimumTeachings(self, n, languages, friendships):
        """
        :param n: int               # number of languages (1..n)
        :param languages: List[List[int]]  # languages[i] = list of langs user (i+1) knows
        :param friendships: List[List[int]] # 1-based user pairs [u, v]
        :return: int  # minimum number of users to teach
        """
        m = len(languages)  # number of users
        # Convert each user's known languages into a set for O(1) test
        lang_sets = [set(lang_list) for lang_list in languages]

        # 1) Find all "bad" friendships (no common language)
        bad_users = set()
        for u, v in friendships:
            u0, v0 = u - 1, v - 1
            if not (lang_sets[u0] & lang_sets[v0]):
                bad_users.add(u0)
                bad_users.add(v0)

        # If no bad friendships, no teaching needed
        if not bad_users:
            return 0

        # 2) For each language L, count how many bad_users need to learn it
        ans = float('inf')
        for L in range(1, n + 1):
            teach_count = 0
            for u in bad_users:
                if L not in lang_sets[u]:
                    teach_count += 1
            ans = min(ans, teach_count)

        return ans
