import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # input: integer array with repeating value
        # output: array of top K frequent values
        # goal: find the top K frequent value
        # -> keep track of value and its frequency -> dict
        # 1. loop thru nums
        # 2. if num(key) in dict, increase value by 1
        # 3. how to get top K?
        # get dict.values() and sort
        # store top K frequency in array
        # back to dict, if value in array, store key

        frequencyDict = collections.defaultdict(lambda: 0)
        for num in nums:
            frequencyDict[num] = frequencyDict[num] + 1
        frequency = sorted(list(frequencyDict.values()), reverse=True)[0:k]
        ans = []
        for key in frequencyDict:
            if frequencyDict[key] in frequency:
                ans.append(key)
        return ans


if __name__ == "__main__":
    nums = [4, 1, -1, 2, -1, 2, 3, 1]
    k = 2
    s = Solution()
    print(s.topKFrequent(nums, k))
