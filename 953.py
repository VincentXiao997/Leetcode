class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(0, len(words) - 1):
            if not self.larger(words[i], words[i+1], order):
                return False
        return True
    
    def larger(self, word1, word2, order):
        # print(word1, word2)
        for i in range(len(word1)):
            if i >= len(word2):
                return False
            # print(word1[i], word2[i])
            if order.find(word1[i]) > order.find(word2[i]):
                return False
            if order.find(word1[i]) < order.find(word2[i]):
                return True
        return True