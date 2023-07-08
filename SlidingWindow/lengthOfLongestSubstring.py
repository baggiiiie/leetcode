class Solution(object):
    def lengthOfLongestSubstring(self, s):
        ans = 0
        l = 0
        for l in range(len(s)):
            traversed = []
            r = l
            while r < len(s):
                if s[r] in traversed:
                    break
                traversed.append(s[r])
                r += 1
            ans = max(ans, len(traversed))
        return ans

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


if __name__ == "__main__":
    strs = ["abcabcbb", "bbbbb", "pwwkew", " ", ""]
    sol = Solution()
    for s in strs:
        print(sol.lengthOfLongestSubstring(s))
