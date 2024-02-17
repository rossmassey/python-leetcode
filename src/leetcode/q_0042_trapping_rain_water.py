from typing import Optional, List, Dict

class Solution0042:
    """
    `Hard <https://leetcode.com/problems/trapping-rain-water/>`_
    ------------------------------------------------------------

    .. sidebar:: Constraints

        * ``n == height.length``
        * ``1 <= n <= 2 * 10^4``
        * ``0 <= height[i] <= 10^5``

    Given ``n`` non-negative integers representing an elevation map where
    the width of each bar is ``1``, compute how much water it can trap
    after raining.

    ------

    :Example 1:

    >>> Solution0042.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1])
    6

    .. image:: https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
        :alt: Diagram representing elevation map for the above heights


    The above elevation map (black section) is represented by array
    ``[0,1,0,2,1,0,1,3,2,1,2,1]``. In this case, 6 units of rain water (blue
    section) are being trapped.


    :Example 2:

    >>> Solution0042.trap(height = [4,2,0,3,2,5])
    9

    """
    @staticmethod
    def trap(height: List[int]) -> int:
        """
        Args:
            height (List[int]): array representing the heights
        Returns:
            int: amount of water trapped between the bars

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            use two pointers ``left`` and ``right`` starting from both
            ends. record max value ``left`` and ``right`` has seen

            move the pointer attached to shorter height inward, since
            that is restricting the ``trapped_water`` amount

            when moving the ``left`` or ``right`` pointer, add the
            amount of water that can be trapped at that index by
            subtracting the current ``height`` from the ``max()`` height
            seen so far (including current)


        """

        left = 0
        left_max = height[left]

        right = len(height) - 1
        right_max = height[right]

        trapped_water = 0
        
        while left < right:
            if height[left] < height[right]:
                left_max = max(height[left], left_max)
                trapped_water += left_max - height[left] 

                left += 1

            else:
                right_max = max(height[right], right_max)
                trapped_water += right_max - height[right] 

                right -= 1
        
        return trapped_water
