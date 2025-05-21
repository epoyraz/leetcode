class Solution(object):
    def entityParser(self, text):
        entities = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": '&',
            "&gt;": '>',
            "&lt;": '<',
            "&frasl;": '/',
        }

        i = 0
        n = len(text)
        result = []
        while i < n:
            if text[i] == '&':
                matched = False
                for entity, char in entities.items():
                    if text.startswith(entity, i):
                        result.append(char)
                        i += len(entity)
                        matched = True
                        break
                if not matched:
                    result.append(text[i])
                    i += 1
            else:
                result.append(text[i])
                i += 1
        return ''.join(result)
