
class Solution:
    def mergeInBetween(self, list1, a, b, list2):
        # 1) Find node just before index a
        prev = list1
        for _ in range(a - 1):
            prev = prev.next

        # 2) Find node just after index b
        post = prev
        for _ in range(b - a + 2):
            post = post.next

        # 3) Splice in list2
        prev.next = list2

        # 4) Find tail of list2
        tail = list2
        while tail.next:
            tail = tail.next

        # 5) Connect tail of list2 to post
        tail.next = post

        return list1