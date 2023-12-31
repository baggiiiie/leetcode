class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # input: int arr
        # output: int
        # note: order of arr cant be changed
        # goal: find the smallest(biggest) diff

        # 1. loop thru arr
        # 2. pointers l and r, find smallest arr[l] - arr[r]
        # 2. or biggest arr[r] - arr[l]
        # 3. store the biggest diff and return

        # it's looping thru arr twice, O(n^2)

        max_profit = 0
        for l, price in enumerate(prices):
            r = l + 1
            while r <= len(prices) - 1:
                profit = prices[r] - price
                if profit > max_profit:
                    max_profit = profit
                r += 1
        return max_profit

    def maxProfit2(self, prices):
        # instead of looping thru the array twice
        # which results in n^2
        # how about sorting array every iteration
        # sorting is logn, then the algo will be nlogn
        max_profit = 0
        r = len(prices) - 1
        for l in range(len(prices) - 1):
            sorted_price = sorted(prices[l + 1 : r + 1])
            # print(prices)
            # print(sorted_price)
            profit = sorted_price[-1] - prices[l]
            if profit > max_profit:
                max_profit = profit
        return max_profit

    def maxProfit3(self, prices):
        max_profit = 0
        lowest_price = prices[0]
        for price in prices:
            lowest_price = min(price, lowest_price)
            max_profit = max(price - lowest_price, max_profit)
        return max_profit


if __name__ == "__main__":
    nums = [[7, 1, 5, 3, 6, 4], [7, 6, 4, 3, 1], [1, 2]]
    s = Solution()
    for num in nums:
        print(s.maxProfit3(num))
