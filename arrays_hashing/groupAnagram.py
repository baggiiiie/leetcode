class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # goal: find and group anagrams
        # return 2d array, including space and single char
        # identify anagram: char and char counts -> dictionary
        # unknown number of words, how many dicts to create?
        # anagram: same char same counts -> after sort, anagrams are the same
