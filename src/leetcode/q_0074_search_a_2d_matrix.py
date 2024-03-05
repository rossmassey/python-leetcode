from typing import Optional, List, Dict

class Solution0074:
    """
    `Medium <https://leetcode.com/problems/search-a-2d-matrix/>`_
    -------------------------------------------------------------

    .. sidebar:: Constraints

        * ``m == matrix.length``
        * ``n == matrix[i].length``
        * ``1 <= m, n <= 100``
        * ``-10^4 <= matrix[i][j], target <= 10^4``

    You are given an ``m x n`` integer matrix ``matrix`` with the following
    two properties:

    * Each row is sorted in non-decreasing order.
    * The first integer of each row is greater than the last integer of the previous row.

    Given an integer ``target``, return ``True`` *if* ``target`` *is in*
    ``matrix`` *or* ``False`` *otherwise*.

    You must write a solution in ``O(log(m * n))`` time complexity.

    ------

    :Example 1:

    .. image:: https://assets.leetcode.com/uploads/2020/10/05/mat.jpg
        :alt: table showing the 2D matrix

    >>> Solution0074.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
    True

    :Example 2:

    .. image:: https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg
        :alt: table showing the 2D matrix

    >>> Solution0074.searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
    False

    """
    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        """
        Args:
            matrix (List[List[int]]): 2D matrix
            target (int): target number to search for
        Returns:
            bool: if target was found

        ------

        :Runtime:   ``O(log(m * n))``
        :Space:     ``O(1)``

        :Strategy:

            treat the 2D array as a 1D array
        
            :math:`\\text{row_index}=\\text{index}\\div\\text{cols}` (how many fit in a
            row)

            :math:`\\text{col_index}=\\text{index}\\pmod{\\text{cols}}`

        """
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = (rows * cols) - 1

        while left <= right:
            middle = left + (right - left) // 2
            element = matrix[middle // cols][middle % cols]

            if element > target:
                right = middle - 1
            elif element < target:
                left = middle + 1
            else:
                return True

        return False

    @staticmethod
    def searchMatrixLinear(matrix: List[List[int]], target: int) -> bool:
        """
        Args:
            matrix (List[List[int]]): 2D matrix
            target (int): target number to search for
        Returns:
            bool: if target was found

        ------

        :Runtime:   ``O(m + n)``
        :Space:     ``O(1)``

        :Strategy:

            simpler, but linear approach

            can use either the top right or bottom left as a starting pivot

            since it is sorted, moving left/up will decrease and moving
            right/down will increase

        """
        # top right
        row, col = 0, len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True

        return False
