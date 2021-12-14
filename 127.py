class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList =list(set(wordList))
        if endWord not in wordList:
            return 0 
        queue = collections.deque([beginWord])
        result = 0
        charStr = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            size = len(queue)
            result += 1
            for _ in range(size):
                currentWord = queue.popleft()
                if currentWord == endWord:
                    return result
                for i in range(len(currentWord)):
                    for c in charStr:
                        newWord = currentWord[:i] + c + currentWord[i+1:]
                        if newWord in wordList:
                            queue.append(newWord)
                            wordList.remove(newWord)
                
        return 0