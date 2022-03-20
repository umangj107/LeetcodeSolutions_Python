# Approach-1

class TrieNode:
    def __init__(self):
        self.links = [None for _ in range(26)]
        self.flag = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if node.links[ord(ch) - ord('a')] != None:
                node = node.links[ord(ch) - ord('a')]
            else:
                node.links[ord(ch) - ord('a')] = TrieNode()
                node = node.links[ord(ch) - ord('a')]

        node.flag = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if node.links[ord(ch) - ord('a')] == None:
                return False
            elif node.links[ord(ch) - ord('a')] != None:
                node = node.links[ord(ch) - ord('a')]

        return node.flag

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if node.links[ord(ch) - ord('a')] == None:
                return False
            elif node.links[ord(ch) - ord('a')] != None:
                node = node.links[ord(ch) - ord('a')]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# Approach-2


class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        curr = self.trie
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr["-"] = True

    def search(self, word: str) -> bool:
        curr = self.trie
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]
        return "-" in curr

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie
        for char in prefix:
            if char not in curr:
                return False
            curr = curr[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
