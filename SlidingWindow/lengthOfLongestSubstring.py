class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # input: string w/ letters
        # output: int

        # two pointers, stop when char[r] = char[l]
        # then l++, r = l + 1
        # but that means O(n^2)
