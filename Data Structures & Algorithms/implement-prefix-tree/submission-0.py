class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.vals:
                curr.vals[word[i]] = PrefixNode()
            if i == len(word) - 1:
                curr.vals[word[i]].exists = True
            curr = curr.vals[word[i]]

    def search(self, word: str) -> bool:
        curr = self.root
        for i in range(len(word)):
            if word[i] not in curr.vals:
                return False
            if i == len(word) - 1:
                if curr.vals[word[i]].exists:
                    return True
                else:
                    return False
            curr = curr.vals[word[i]]

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i in range(len(prefix)):
            if prefix[i] not in curr.vals:
                return False
            if i == len(prefix) - 1:
                return True
            curr = curr.vals[prefix[i]]
        
class PrefixNode:

    def __init__(self):
        self.exists = False
        self.vals = {}