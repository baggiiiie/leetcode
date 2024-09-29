class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # input: string
        # output: int, length of longest sub string after replacement
        # solution:
        # - keep track of most frequent char in the sub string (window)
        # - if char_to_replace > k, window invalid, move l
        # - char_to_replace = window_size - most_frequent_char_in_window
        # 1. loop thru string, two pointers; hashmap keep track of char count
        # 2. move r pointer, look up map to check window valid
        # 3. invalid: move l pointer, decrease window char count
        # 4. keep track of max_len
        max_len = 0
        char_count = {}
        l = 0
        for r, char in enumerate(s): # TC: O(n)
            char_count[char] = char_count.get(char, 0) + 1  # SC: O(n) O(26)
            win_size = r - l + 1
            if win_size - max(char_count.values()) > k: # TC: O(26)
                char_count[s[l]] -= 1
                l += 1
            else:
                max_len = max(win_size, max_len)

        return max_len

if __name__ == '__main__':
    s = "AAABABB"
    k = 1
    solution = Solution()
    res = solution.characterReplacement(s, k)
    print(res)
