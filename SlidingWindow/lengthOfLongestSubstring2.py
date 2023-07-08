class Solution(object):
    # the idea of the following code is
    # if s[r] exists in the substring, get its index in the substring
    # and remove everything before the char, inlucding the char
    # to get the index, is to remove everything before the index
    # hence need a find function to get index
    # if use set, we can accomplish deletion w/o indexes
    def lengthOfLongestSubstring2(self, s):
        ans = 0
        substring = []
        for l in range(len(s)):
            i, found = self.findIndex(substring, s[l])
            if found:
                substring = substring[i + 1 :]
            substring.append(s[l])
            ans = max(ans, len(substring))
        return ans

    def findIndex(self, str, target):
        for i, s in enumerate(str):
            if target == s:
                return i, True
        return 0, False

    # lets use set this time
    # 1. l, r pointers loop thru string
    # 2. store traversed char in a charSet
    # 3. if char in charSet, delete everything in the substring from left
    # until char isnt in charSet
    # 4. the substring is THE sliding window
    # 5. compare res and r - l + 1
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        charSet = set()
        l = 0
        for r, char in enumerate(s):
            while char in charSet:
                charSet.remove(s[l])
                l += 1  # this is how to 'delete' the substring
                # it basically empties charSet moves l to where r is
            charSet.add(char)
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    strs = ["abcabcbb", "bbbbb", "pwwkew", " ", "", "dabbcfe"]
    sol = Solution()
    for s in strs:
        print(sol.lengthOfLongestSubstring(s))
