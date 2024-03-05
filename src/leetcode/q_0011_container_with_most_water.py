from typing import Optional, List, Dict

class Solution0011:
    """
    `Medium <https://leetcode.com/problems/container-with-most-water/>`_
    --------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``n == height.length``
        * ``2 <= n <= 10^5``
        * ``0 <= height[i] <= 10^4``

    You are given an integer array ``height`` of length ``n``. There are ``n``
    vertical lines drawn such that the two endpoints of the ``i^th`` line are
    ``(i, 0)`` and ``(i, height[i])``.

    Find two lines that together with the x-axis form a container, such that
    the container contains the most water.

    Return *the maximum amount of water a container can store*.

    **Notice** that you may not slant the container.

    ------

    :Example 1:

    .. image:: https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg
        :alt: Diagram representing above heights

    >>> Solution0011.maxArea(height = [1,8,6,2,5,4,8,3,7])
    49

    The above vertical lines are represented by array ``[1,8,6,2,5,4,8,3,7]``.
    In this case, the max area of water (blue section) the container can
    contain is ``49``.


    :Example 2:

    >>> Solution0011.maxArea(height = [1,1])
    1

    """
    @staticmethod
    def maxArea(height: List[int]) -> int:
        """
        Args:
            height (List[int]): array representing the heights
        Returns:
            int: the max amount of water contained

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            use two pointers, ``left`` and ``right``, starting from the ends

            calculate the amount of water that can be stored between ``left``
            and ``right``, using the smaller ``height`` (after which the water
            overflows)

            track the ``max()`` amount of water

            advance the pointer on the smaller ``height``, since it is the
            limiting factor in maximizing area

        """

        max_water_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            limiting_height = min(height[left], height[right])

            current_area = limiting_height * width
            max_water_area = max(max_water_area, current_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water_area
