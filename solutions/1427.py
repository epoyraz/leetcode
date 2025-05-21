class Solution:
    def getAllElements(self, root1, root2):
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        list1 = inorder(root1)
        list2 = inorder(root2)
        
        # Merge the two sorted lists
        merged = []
        i = j = 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged
