from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        # Map file content to list of full file paths
        content_map = defaultdict(list)
        
        for entry in paths:
            parts = entry.split(' ')
            root = parts[0]
            # Each subsequent part is "filename(content)"
            for file_info in parts[1:]:
                name, rest = file_info.split('(')
                content = rest[:-1]  # strip the trailing ')'
                full_path = root + '/' + name
                content_map[content].append(full_path)
        
        # Only keep groups with more than one file (duplicates)
        return [group for group in content_map.values() if len(group) > 1]
