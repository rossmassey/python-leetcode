from typing import Optional, List, Dict
from collections import namedtuple

class Solution0084:
    """
    `Hard <https://leetcode.com/problems/largest-rectangle-in-histogram/>`_
    -----------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``1 <= heights.length <= 10^5``
        * ``0 <= heights[i] <= 10^4``

    Given an array of integers ``heights`` representing the histogram's bar
    height where the width of each bar is ``1``, return *the area of the largest
    rectangle in the histogram*.

    ------

    :Example 1:

    .. image:: https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg
        :alt: Diagram representing example 1 histogram, highlighting areas

    >>> Solution0084.largestRectangleArea(heights = [2,1,5,6,2,3])
    10

    The above is a histogram where width of each bar is 1.
    The largest rectangle is shown in the red area, which has an area = 10 units.


    :Example 2:

    .. image:: https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg
        :alt: Diagram representing example 2 histogram, highlighting areas

    >>> Solution0084.largestRectangleArea(heights = [2,4])
    4

    """
    @staticmethod
    def largestRectangleArea(heights: List[int]) -> int:
        """
        Args:
            heights (List[int]): histogram's bar height
        Returns:
            int: largest rectangle in histogram

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            starting from left, add each ``Edge`` to a stack

            if a previous edge is lower than a later edge it can no longer be
            utilized, so ``pop`` previous ones and calculate potential areas

            track ``max`` rectangle area seen so far

            add the later edge and how far back its ``height`` can extend (since
            that will be included in the rectangle area)

            process stack for areas at end, stack will contain the edges
            that never had a lower subsequent edge height (so their rectangle
            area extends to final element in array)

        """
        # represents the edge of a rectangle
        Edge = namedtuple('Edge', 'start_index height')

        # will maintain a monotonic increasing stack
        extendable_edges = []
        max_area = 0

        for current_index, height in enumerate(heights):
            start_current_height = current_index

            # if a previous edge at or above current height
            while extendable_edges and extendable_edges[-1].height >= height:
                prev_edge = extendable_edges.pop()

                # can calculate its area extended to current index
                width = current_index - prev_edge.start_index
                extended_area = width * prev_edge.height
                max_area = max(max_area, extended_area)

                # record that the current height extends backward
                start_current_height = prev_edge.start_index
            
            # add furthest left edge of current height
            extendable_edges.append(Edge(start_current_height, height))

        # remaining edges had no subsequent bar of lower height
        for edge in extendable_edges:
            # so their area extends to right bound
            width = len(heights) - edge.start_index
            max_area = max(max_area, width * edge.height)
        
        return max_area
