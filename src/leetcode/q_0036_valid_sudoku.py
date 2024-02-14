from typing import Optional, List, Dict

class Solution0036:
    """
    `Medium <https://leetcode.com/problems/valid-sudoku/>`_
    -------------------------------------------------------

    .. sidebar:: Constraints

        * ``board.length == 9``
        * ``board[i].length == 9``
        * ``board[i][j]`` is a digit ``1-9`` or ``'.'``

    Determine if a ``9 x 9`` Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:

    * Each row must contain the digits ``1-9`` without repetition.
    * Each column must contain the digits ``1-9`` without repetition.
    * Each of the nine ``3 x 3`` sub-boxes of the grid must contain the digits ``1-9`` without repetition.

    **Note:**

    * A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    * Only the filled cells need to be validated according to the mentioned rules.

    ------

    :Example 1:

    >>> Solution0036.isValidSudoku(board = [
    ... ["5","3",".",".","7",".",".",".","."],
    ... ["6",".",".","1","9","5",".",".","."],
    ... [".","9","8",".",".",".",".","6","."],
    ... ["8",".",".",".","6",".",".",".","3"],
    ... ["4",".",".","8",".","3",".",".","1"],
    ... ["7",".",".",".","2",".",".",".","6"],
    ... [".","6",".",".",".",".","2","8","."],
    ... [".",".",".","4","1","9",".",".","5"],
    ... [".",".",".",".","8",".",".","7","9"]])
    True


    :Example 2:

    >>> Solution0036.isValidSudoku(board = [
    ... ["8","3",".",".","7",".",".",".","."],
    ... ["6",".",".","1","9","5",".",".","."],
    ... [".","9","8",".",".",".",".","6","."],
    ... ["8",".",".",".","6",".",".",".","3"],
    ... ["4",".",".","8",".","3",".",".","1"],
    ... ["7",".",".",".","2",".",".",".","6"],
    ... [".","6",".",".",".",".","2","8","."],
    ... [".",".",".","4","1","9",".",".","5"],
    ... [".",".",".",".","8",".",".","7","9"]])
    False

    Same as Example 1, except with the **5** in the top left corner being
    modified to **8**. Since there are two 8's in the top left 3x3 sub-box, it
    is invalid.

    """
    @staticmethod
    def isValidSudoku(board: List[List[str]]) -> bool:
        """
        Args:
            board (List[List[str]]): sudoku board
        Returns:
            bool: if it is valid

        ------

        :Runtime:   ``O(n^2) = O(9*9)``
        :Space:     ``O(n)``

        :Strategy:

            use a single ``set`` to track seen numbers

            iterate through each ``num`` on the board, keyed by its ``row`` number,
            ``col`` number, and ``square`` index prefixed to the number itself
            (so key is unique)

            if any ``keys`` has already been seen, the board is not valid

        """
        seen = set()

        for row, nums in enumerate(board):
            for col, num in enumerate(nums):
                if num == '.':
                    continue

                row_key = f'r{row}:{num}'
                col_key = f'c{col}:{num}'
                square_key = f's{row // 3},{col // 3}:{num}'

                keys = {row_key, col_key, square_key}

                # if set intersection (is not empty)
                if keys & seen:
                    return False

                seen.update(keys)

        return True
