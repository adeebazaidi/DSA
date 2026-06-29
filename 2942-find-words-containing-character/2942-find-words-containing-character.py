class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        List=[]
        for i in range(len(words)):
            if x in words[i]:
                List.append(i)
        return List