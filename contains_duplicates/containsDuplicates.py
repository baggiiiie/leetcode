class Solution(object):
    def containsDuplicate(self, nums):
        """
        The goal is to find if an array contains duplicates
        Returns true or false accordingly
        - use a dict to keep track of the count of every number while looping thru the array
        1. create dict
        2. loop thru
        3. check if num in arr
        4. update dict if not in 
        """
        numDict = {}
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num] = 0

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 9, 8, 7, 6, 0, 1]
    s = Solution()
    print(s.containsDuplicate(numbers))