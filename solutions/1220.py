class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        from collections import defaultdict

        skill_index = {skill: i for i, skill in enumerate(req_skills)}
        n_skills = len(req_skills)

        # Convert each person's skills to a bitmask
        people_masks = []
        for p in people:
            mask = 0
            for skill in p:
                mask |= 1 << skill_index[skill]
            people_masks.append(mask)

        dp = {0: []}  # key = skill bitmask, value = list of people indices

        for i, person_mask in enumerate(people_masks):
            new_dp = dp.copy()
            for skill_set, team in dp.items():
                combined = skill_set | person_mask
                if combined not in new_dp or len(new_dp[combined]) > len(team) + 1:
                    new_dp[combined] = team + [i]
            dp = new_dp

        full_mask = (1 << n_skills) - 1
        return dp[full_mask]
