class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # goal: check if a word is palindrome
        # read from both ends, stop when two pointers meet
        # stop when pointed char are different

        # deal with special characters:
        # 1. copy the string without special char
        # 2. jump ahead when it's special char
        # deal with two special characters back to back

        s = s.lower()
        c = ""
        for char in s: 
            if char.isalnum():
                c += char
        l = 0
        r = len(c) - 1
        while l != r:
            # print (c[l], c[r])
            if c[l] != c[r]:
                return False
            l += 1 
            r -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    word = "A man, a plan, a canal: Panama"
    print(s.isPalindrome(word))