from typing import Optional, List, Dict

class Solution0121:
    """
    `Easy <https://leetcode.com/problems/best-time-to-buy-and-sell-stock/>`_
    ------------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= prices.length <= 10^5``
        * ``0 <= prices[i] <= 10^4``

    You are given an array ``prices`` where ``prices[i]`` is the price of a
    given stock on the ``i^th`` day.

    You want to maximize your profit by choosing a **single day** to buy one
    stock and choosing a **different day in the future** to sell that stock.

    Return *the maximum profit you can achieve from this transaction*. If you
    cannot achieve any profit, return ``0``.



    ------

    :Example 1:

    >>> Solution0121.maxProfit(prices = [7,1,5,3,6,4])
    5

    Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

    Note that buying on day 2 and selling on day 1 is not allowed because you
    must buy before you sell.


    :Example 2:

    >>> Solution0121.maxProfit(prices = [7,6,4,3,1])
    0

    In this case, no transactions are done and the max profit = 0.

    """
    @staticmethod
    def maxProfit(prices: List[int]) -> int:
        """
        Args:
            prices (List[int]): stock prices over a period of time
        Returns:
            int: max profit to be made from buying and selling once

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            track the ``lowest_price`` seen

            for each day's ``current_price``, check if lower than previous
            lowest and update if needed

            else if not currently at lowest price, check if ``profit`` made
            by selling today (after buying on lowest day) is greater than
            ``max_profit``

        """
        max_profit = 0
        lowest_price = prices[0]

        for current_price in prices:
            if current_price < lowest_price:
                lowest_price = current_price

            elif (profit := current_price - lowest_price) > max_profit:
                max_profit = profit
                
        return max_profit

