import heapq

class Solution(object):
     def minimumCost(self, nums, k, dist):
         import heapq
         n = len(nums)
         id_of_index = [0] * n
         maxA = []      # max-heap (store negatives) of the current k-1 smallest
         minB = []      # min-heap of the rest
         id2set = {}    # maps id -> 'A' or 'B'
         removed = set()
         sizeA = sizeB = 0
         sumA = 0
         uid = 0

         def pruneA():
             while maxA:
                 val, iid = maxA[0]
                 if iid in removed:
                     heapq.heappop(maxA)
                     removed.remove(iid)
                 else:
                     break

         def pruneB():
             while minB:
                 val, iid = minB[0]
                 if iid in removed:
                     heapq.heappop(minB)
                     removed.remove(iid)
                 else:
                     break

         # --- build the initial window [1..r] exactly as before ---
         r = min(n-1, dist+1)
         for i in xrange(1, r+1):
             x = nums[i]
             uid += 1
             iid = uid
             id_of_index[i] = iid
             if sizeA < k-1:
                 heapq.heappush(maxA, (-x, iid))
                 id2set[iid] = 'A'
                 sizeA += 1
                 sumA += x
             else:
                 pruneA()
                 maxA_val = -maxA[0][0]
                 if x < maxA_val:
                     # swap out the current largest of A
                     neg_y, yid = heapq.heappop(maxA)
                     y = -neg_y
                     sizeA -= 1
                     sumA -= y
                     heapq.heappush(minB, (y, yid))
                     id2set[yid] = 'B'
                     sizeB += 1
                     # insert the new x into A
                     heapq.heappush(maxA, (-x, iid))
                     id2set[iid] = 'A'
                     sizeA += 1
                     sumA += x
                 else:
                     heapq.heappush(minB, (x, iid))
                     id2set[iid] = 'B'
                     sizeB += 1

         ans = float('inf')
         prev_r = r

         # --- slide the window's left edge from 1 up to n-k+1 ---
         for l in xrange(1, n - k + 2):
             ans = min(ans, sumA)
             if l == n - k + 1:
                 break

             # remove the outgoing index l
             iid_out = id_of_index[l]
             if id2set[iid_out] == 'A':
                 sizeA -= 1
                 sumA -= nums[l]
             else:
                 sizeB -= 1
             removed.add(iid_out)

             # add the new element at prev_r+1, if any
             if prev_r < n - 1:
                 new_r = prev_r + 1
                 x = nums[new_r]
                 uid += 1
                 nid = uid
                 id_of_index[new_r] = nid

                 # **always** compare to max of A, then push
                 pruneA()
                 pruneB()
                 if maxA and x < -maxA[0][0]:
                     heapq.heappush(maxA, (-x, nid))
                     id2set[nid] = 'A'
                     sizeA += 1
                     sumA += x
                 else:
                     heapq.heappush(minB, (x, nid))
                     id2set[nid] = 'B'
                     sizeB += 1

                 prev_r = new_r

             # now rebalance to restore sizeA == k-1
             pruneA()
             pruneB()
             while sizeA < k-1:
                 pruneB()
                 y, yid = heapq.heappop(minB)
                 sizeB -= 1
                 heapq.heappush(maxA, (-y, yid))
                 id2set[yid] = 'A'
                 sizeA += 1
                 sumA += y
             while sizeA > k-1:
                 pruneA()
                 neg_y, yid = heapq.heappop(maxA)
                 y = -neg_y
                 sizeA -= 1
                 sumA -= y
                 heapq.heappush(minB, (y, yid))
                 id2set[yid] = 'B'
                 sizeB += 1

         return nums[0] + ans
