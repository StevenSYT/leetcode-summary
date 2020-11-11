#
# @lc app=leetcode id=1125 lang=python3
#
# [1125] Smallest Sufficient Team
#

# @lc code=start
from collections import deque


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        queue = deque([(set(req_skills), set())])

        while queue:
            target_skills, cur_team = queue.popleft()
            for idx, person in enumerate(people):
                if idx in cur_team:
                    continue
                # We need solve/remove all skills in the skillset,
                # so why not just only care about people who has
                # the first skill in target_skills.
                # note that since we cannot index through set, we need
                # to use this next(iter(S)) to access one item in set.
                # TC for next(iter(S)) is O(1) --- needs confirmation.
                if next(iter(target_skills)) not in person:
                    continue
                next_target = target_skills.copy()
                for skill in person:
                    if skill in next_target:
                        next_target.remove(skill)
                if len(next_target) == 0:
                    return cur_team | {idx}
                queue.append((next_target, cur_team | {idx}))


class Solution1:
    def smallestSufficientTeam(self, req_skills: List[str],
                               people: List[List[str]]) -> List[int]:
        n = len(req_skills)

        # Create a mapping from skill to skill index, this will be useful to use the bitmask
        skill_set = {skill: idx for idx, skill in enumerate(req_skills)}

        # dp here is a dict, with status as the key, optimal team as the value.
        
        # For the status, we use binary number indicating the status of the
        # completion of the skill set.
        
        # For example if req_skill has 5 elements, 10010 can indicate one status
        # of the completion of the skill set: the first and the fourth skills are covered
        # with the current team.
        dp = {0: []}

        for idx, person in enumerate(people):
            person_skills = 0
            for skill in person:
                # skip skills not in the skill_set.
                if skill not in skill_set:
                    continue
                i = skill_set[skill]
                # update his_skill using bit operation.
                person_skills += 1 << i
            for status, team in list(dp.items()):
                next_status = status | person_skills
                # No new skill can be covered from this person, skip.
                if next_status == status:
                    continue
                # update the dp with new entry or better entry for target status.
                if next_status not in dp or len(
                        dp[next_status]) > len(dp[status]) + 1:
                    dp[next_status] = team + [idx]
        return dp[(1 << n) - 1]


# @lc code=end
