class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # goal: check if s and t have the exact number of the same characters
        # save s and t char into dict, and keep track of the char count
        # 1. create dict and save s with char count
        # 2. same for t
        # 3. compare the dict

        # now how to improve run time? currently it's linear time
        # memory wise, do we really need 2 dictionaries?
        sDict = {}
        tDict = {}
        if len(s) != len(t):
            return False
        for char in s:
            sDict[char] = sDict.get(char, 0) + 1
        for char in t:
            tDict[char] = tDict.get(char, 0) + 1
        if sDict == tDict:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    string1 = 'anagram'
    string2 = 'nagaraa'
    print(s.isAnagram(string1, string2))