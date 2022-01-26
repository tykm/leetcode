class WordDictionary:
    

    def __init__(self):
        self.trie = {}
        
    def addWord(self, word: str) -> None:
        node = self.trie
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['$'] = True
        
    def search(self, word: str) -> bool:
        node = self.trie
        for letter in word:
            if letter == '.':
                # Need to check every possible child recursively
                pass
            if letter in node:
                node = node[letter]
        
        
        return '$' in node
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)