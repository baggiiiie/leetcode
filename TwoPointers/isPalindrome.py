class Solution(object):
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # goal: check if a word is palindrome
        # read from both ends, stop when two pointers meet
        # stop when pointed char are different

        # deal with special characters:
        # 1. copy the string without special char

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

    def isPalindrome2(self, s):
            """
            :type s: str
            :rtype: bool
            """
            # goal: check if a word is palindrome
            # read from both ends, stop when two pointers meet
            # stop when pointed char are different

            # deal with special characters:
            # 2. jump ahead when it's special char
            # deal with two special characters back to back

            s = s.lower()
            l, r = 0, len(s) - 1
            while l < r:
                while l < r and not s[l].isalnum():
                    l += 1 
                while l < r and not s[r].isalnum():
                    r -= 1
                # print(s[l], s[r])
                if s[l] != s[r]:
                    return False
                l += 1 
                r -= 1
            return True

if __name__ == '__main__':
    s = Solution()
    word = "A man, a plan, a canal: Panama"
    print(s.isPalindrome2(word))