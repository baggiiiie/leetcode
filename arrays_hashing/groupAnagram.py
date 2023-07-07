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
        # tea, ate, eat -> aet
        # loop thru list, sort each word, compare each word with those in the list
        # empty string and single word string are to be return too
        # 1. loop thru list
        # 2. compare sorted word with dict
        # 3. if sorted word in key, add to value,
        # else sorted word is new key with unsorted word as value
        # 4. return value of every key in dict

        anagramDict = {}
        result = []
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anagramDict:
                anagramDict[sorted_word].append(word)
            else:
                anagramDict[sorted_word] = [word]
        for key in anagramDict:
            result.append(anagramDict[key])

        return result


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))
