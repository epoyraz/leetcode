class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        name_map = {}
        result = []

        for name in names:
            if name not in name_map:
                name_map[name] = 1
                result.append(name)
            else:
                k = name_map[name]
                while True:
                    new_name = "%s(%d)" % (name, k)
                    if new_name not in name_map:
                        break
                    k += 1
                result.append(new_name)
                name_map[name] = k + 1
                name_map[new_name] = 1

        return result
