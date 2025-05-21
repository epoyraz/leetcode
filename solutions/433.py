from collections import deque

class Solution:
    def minMutation(self, startGene, endGene, bank):
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        queue = deque([(startGene, 0)])
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            gene, steps = queue.popleft()
            if gene == endGene:
                return steps
            for i in range(len(gene)):
                for g in genes:
                    if g != gene[i]:
                        next_gene = gene[:i] + g + gene[i+1:]
                        if next_gene in bank_set:
                            queue.append((next_gene, steps + 1))
                            bank_set.remove(next_gene)
        
        return -1
