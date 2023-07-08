class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # input: string
        # output: int

        # two pointers, stop when char[r] = char[l]
        # then l++, r = l + 1
        # but that means O(n^2)

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


if __name__ == "__main__":
    strs = ["abcabcbb", "bbbbb", "pwwkew", " ", ""]
    sol = Solution()
    for s in strs:
        print(sol.lengthOfLongestSubstring(s))
