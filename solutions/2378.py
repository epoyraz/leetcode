class Solution:
    def largestWordCount(self, messages, senders):
        counts = {}
        for msg, sender in zip(messages, senders):
            # Count words by counting spaces + 1
            wc = msg.count(' ') + 1
            counts[sender] = counts.get(sender, 0) + wc
        
        # Find the sender with max count, breaking ties by lex order
        best_sender = None
        best_count = -1
        for sender, cnt in counts.items():
            if cnt > best_count or (cnt == best_count and sender > best_sender):
                best_count = cnt
                best_sender = sender
        
        return best_sender
