class WordDictionary(object):

    def __init__(self):
        self.hm = dict()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        if len(word) not in self.hm:
            self.hm[len(word)] = [word]
        else:
            self.hm[len(word)].append(word)

    def match(self, lst, w, ans):
        for i in lst:
            if not w[i] == ans[i]:
                return False
        return True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        idx = []

        if len(word) not in self.hm:
            return False

        if word in self.hm[len(word)]:
            return True

        for i in range(len(word)):
            if word[i] != '.':
                idx.append(i)

        for i in self.hm[len(word)]:
            if self.match(idx, word, i):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
