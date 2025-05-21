class TextEditor:
    def __init__(self):
        self.left = []
        self.right = []

    def addText(self, text):
        for ch in text:
            self.left.append(ch)

    def deleteText(self, k):
        removed = min(k, len(self.left))
        for _ in range(removed):
            self.left.pop()
        return removed

    def cursorLeft(self, k):
        move = min(k, len(self.left))
        for _ in range(move):
            self.right.append(self.left.pop())
        return ''.join(self.left[-10:])

    def cursorRight(self, k):
        move = min(k, len(self.right))
        for _ in range(move):
            self.left.append(self.right.pop())
        return ''.join(self.left[-10:])
