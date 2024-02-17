from typing import Optional, List, Dict

class Solution0739:
    """
    `Medium <https://leetcode.com/problems/daily-temperatures/>`_
    -------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= temperatures.length <= 10^5``
        * ``30 <= temperatures[i] <= 100``

    Given an array of integers ``temperatures`` represents the daily
    temperatures, return *an array* ``answer`` *such that* ``answer[i]`` *is
    the number of days you have to wait after the* ``i^th`` *day to get a
    warmer temperature*. If there is no future day for which this is possible,
    keep ``answer[i] == 0`` instead.

    ------

    :Example 1:

    >>> Solution0739.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73])
    [1, 1, 4, 2, 1, 1, 0, 0]


    :Example 2:

    >>> Solution0739.dailyTemperatures(temperatures = [30,40,50,60])
    [1, 1, 1, 0]


    :Example 3:

    >>> Solution0739.dailyTemperatures(temperatures = [30,60,90])
    [1, 1, 0]

    """
    @staticmethod
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        """
        Args:
            temperatures (List[int]): list of daily temperatures
        Returns:
            List[int]: list of days until warmer temp for each day

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            use a stack to track the previous ``cold_days``, storing just the
            day and not the temperature

            if the top of ``cold_days`` is colder than the current day, pop
            from stack and calculate how many days it took to reach warmer day

            note current day warmer than all previous days on stack, because
            each day in stack is colder than previous one (monotonic
            decreasing). this means all days will be matched with correct
            warmer day if it exists (won't skip any)

            add current day after processing any days colder than today

        """
        days_until_warmer = [0] * len(temperatures)

        # store day index in stack, use temperatures to get that days temp
        cold_days = []

        for current_day, current_temp in enumerate(temperatures):
            # if today is warmer than the last cold day
            while cold_days and temperatures[cold_days[-1]] < current_temp:
                # pop from stack and set that day's answer to how long ago it was
                colder_day = cold_days.pop()
                days_until_warmer[colder_day] = current_day - colder_day

            # else no other days (or no days that were colder), so add to stack
            cold_days.append(current_day)
        
        return days_until_warmer
