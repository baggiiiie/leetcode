class Solution(object):
    """
    Perform a Quicksort then compare if there are consecutive same numbers
    """

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sorted_nums = self.quicksort(nums)
        print(sorted_nums)
        return self.compare(sorted_nums)

    def quicksort(self, arr):
        """
        Quicksort: select a number as pivot, compare the rest with
        this number and put them into left or right array
        Put sorted items into a new array and return this new array
        """
        if len(arr) <= 1:  # stopping condition
            return arr
        pivot = arr[0]
        left_arr = []
        right_arr = []
        for i in arr[1:]:
            if i <= pivot:
                left_arr.append(i)
            else:
                right_arr.append(i)
        return self.quicksort(left_arr) + [pivot] + self.quicksort(right_arr)

    def compare(self, arr):
        """
        Finds if there are consecutive numbers
        Returns true if there are
        """
        if len(arr) <= 1:
            return False
        elif arr[0] == arr[1]:
            return True
        return self.compare(arr[1:])


if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 9, 8, 7, 6, 0, 1]
    s = Solution()
    print(s.containsDuplicate(numbers))