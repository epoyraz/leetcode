class Solution:
    def survivedRobotsHealths(self, positions, healths, directions):
        # Prepare robots sorted by position ascending
        robots = sorted(
            [(pos, i, healths[i], directions[i]) for i, pos in enumerate(positions)],
            key=lambda x: x[0]
        )
        
        stack = []   # stack of (orig_index, health) for 'R' robots
        survivors = []  # list of (orig_index, final_health) for surviving 'L' robots
        
        for _, idx, hp, d in robots:
            if d == 'R':
                stack.append([idx, hp])
            else:  # d == 'L'
                cur_hp = hp
                # collide with any R-robots on stack
                while stack and cur_hp > 0:
                    top_idx, top_hp = stack[-1]
                    if top_hp < cur_hp:
                        # top dies
                        stack.pop()
                        cur_hp -= 1
                    elif top_hp == cur_hp:
                        # both die
                        stack.pop()
                        cur_hp = 0
                    else:  # top_hp > cur_hp
                        # current dies, top loses 1 hp
                        stack[-1][1] -= 1
                        cur_hp = 0
                # if it survived all collisions, record it
                if cur_hp > 0:
                    survivors.append((idx, cur_hp))
        
        # any R-robots left on stack survive with their updated health
        for idx, hp in stack:
            survivors.append((idx, hp))
        
        # sort survivors by original index and return healths
        survivors.sort(key=lambda x: x[0])
        return [hp for _, hp in survivors]
