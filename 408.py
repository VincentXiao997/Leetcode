class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        abbrLen = 0
        while i < len(word) and j < len(abbr):
            print(i, j)
            if word[i] == abbr[j]:
                i+=1
                j+=1
                abbrLen += 1
            elif abbr[j].isnumeric():
                if abbr[j] == "0":
                    return False
                num = int(abbr[j])
                j+=1
                while j < len(abbr) and abbr[j].isnumeric():
                    num = num * 10 + int(abbr[j])
                    j+=1
                i += num
                abbrLen += num
                if i > len(word):
                    return False
            else:
                return False
        # print(abbrLen, len(word))
        if abbrLen != len(word) or j < len(abbr) or i < len(word):
            return False
        else:
            return True
      