from typing import Optional, List, Dict
import math

class Solution0875:
    """
    `Medium <https://leetcode.com/problems/koko-eating-bananas/>`_
    --------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= piles.length <= 10^4``
        * ``piles.length <= h <= 10^9``
        * ``1 <= piles[i] <= 10^9``

    Koko loves to eat bananas. There are ``n`` piles of bananas, the ``i^th``
    pile has ``piles[i]`` bananas. The guards have gone and will come back in
    ``h`` hours.

    Koko can decide her bananas-per-hour eating speed of ``k``. Each hour, she
    chooses some pile of bananas and eats ``k`` bananas from that pile. If the
    pile has less than ``k`` bananas, she eats all of them instead and will not
    eat any more bananas during this hour.

    Koko likes to eat slowly but still wants to finish eating all the bananas
    before the guards return.

    Return *the minimum integer* ``k`` *such that she can eat all the bananas
    within* ``h`` *hours*.

    ------

    :Example 1:

    >>> Solution0875.minEatingSpeed(piles = [3,6,7,11], h = 8)
    4


    :Example 2:

    >>> Solution0875.minEatingSpeed(piles = [30,11,23,4,20], h = 5)
    30


    :Example 3:

    >>> Solution0875.minEatingSpeed(piles = [30,11,23,4,20], h = 6)
    23

    """
    @staticmethod
    def minEatingSpeed(piles: List[int], h: int) -> int:
        """
        Args:
            piles (List[int]): piles of banana
            h (int): hours to eat the bananas
        Returns:
            int: minmimum eating speed

        ------

        :Runtime:   ``O(n log m)``, ``m`` is max element in ``piles``
        :Space:     ``O(1)``

        :Strategy:

            if ``h`` is greater than or equal to ``sum(piles)``, then ``1`` is
            the minimum ``eating_speed``

            if ``h`` is equal to ``len(piles)`` (the smallest it can be to still
            finish), then ``max(piles)`` (max element in ``piles``) is the
            minimum ``eating_speed``

            perform a binary search between ``1`` and ``max(piles)`` to check
            different ``eating_speed`` against ``h``

            calculate ``elapsed_time`` for eating every pile at that speed,
            compare to ``h``

            if ``elapsed_time > h``, need to eat faster, set ``left`` pointer to
            be bigger than current ``eating_speed``

            else have extra time, can eat slower, so set ``right`` pinter to be
            current ``eating_speed``

        """
        
        left = 1
        right = max(piles)
        
        while left < right:
            eating_speed = (left + right) // 2
            elapsed_time = 0

            for pile in piles:
                # ceil since takes 1hr to finish partial value
                pile_time = math.ceil(pile / eating_speed)
                elapsed_time += pile_time

            if elapsed_time > h:
                left = eating_speed + 1
            else:
                right = eating_speed
        
        # ending left pointer is minimum speed that is viable
        return left
