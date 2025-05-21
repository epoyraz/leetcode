class Solution(object):
    def canAliceWin(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 10:
            return False
        
        stones = n
        stones -= 10  # Alice's first move
        if stones < 0:
            return False
        next_move = 9  # Bob's next move should be 9
        
        turn = 1  # 0 for Alice's turn, 1 for Bob's. But let's track whose turn it is. Wait, after Alice's first move, it's Bob's turn.
        
        while True:
            if turn % 2 == 1:  # Bob's turn
                if stones >= next_move:
                    stones -= next_move
                    next_move = next_move - 1
                    turn += 1
                else:
                    return True  # Bob can't move, Alice wins
            else:  # Alice's turn
                if stones >= next_move:
                    stones -= next_move
                    next_move = next_move - 1
                    turn += 1
                else:
                    return False  # Alice can't move, Bob wins