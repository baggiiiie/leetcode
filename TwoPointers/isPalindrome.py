class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # goal: check if a word is palindrome
        # read from both ends, stop when two pointers meet
        # stop when pointed char are different
        # two pointers are moving at the same speed
        l = 0
        r = len(s) - 1
        while l != r:
            if s[l] != s[r]:
                return False
            l += 1 
            r -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    word = 'aba'
    print(s.isPalindrome(word))