class Solution:
    def arrayPositionOfLetter(self, letter: str) -> int:
        return ord(letter) - ord('a')

    def constructCountArrayFromString(self, string: str) -> int[26]:
        array = [0] * 26
        for letter in string:
            array[self.arrayPositionOfLetter(letter)] = array[self.arrayPositionOfLetter(letter)] + 1
        return array

    def isAnagram(self, s: str, t: str) -> bool:
        sArray = self.constructCountArrayFromString(s)
        tArray = self.constructCountArrayFromString(t)

        for i in range(len(sArray)):
            if sArray[i] != tArray[i]:
                return False
            
        return True
