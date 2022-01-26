class WordDictionary:
    

    def __init__(self):
        # { 3: {"bad", "pad", ...},  ...}
        self.d = defaultdict(set)
        
    def addWord(self, word: str) -> None:
        self.d[len(word)].add(word)

    def search(self, word: str) -> bool:
        l = len(word)
        for entry in self.d[l]:
            i = 0
            while i < l and (word[i] == entry[i] or word[i] == '.'):
                i += 1
            if i == l:
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)