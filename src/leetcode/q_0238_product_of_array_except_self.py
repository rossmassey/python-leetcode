from typing import Optional, List, Dict

class Solution0238:
    """
    `Medium <https://leetcode.com/problems/product-of-array-except-self/>`_
    -----------------------------------------------------------------------

    .. sidebar:: Constraints

        * ``2 <= nums.length <= 10^5``
        * ``-30 <= nums[i] <= 30``
        * The product of any prefix or suffix of ``nums`` is **guaranteed** to fit in a **32-bit** integer.

    Given an integer array ``nums``, return *an array* ``answer`` *such that*
    ``answer[i]`` *is equal to the product of all the elements of* ``nums``
    *except* ``nums[i]``.

    The product of any prefix or suffix of ``nums`` is **guaranteed** to fit
    in a **32-bit** integer.

    You must write an algorithm that runs in ``O(n)`` time and without
    using the division operation.

    ------

    :Example 1:

    >>> Solution0238.productExceptSelf(nums = [1,2,3,4])
    [24, 12, 8, 6]


    :Example 2:

    >>> Solution0238.productExceptSelf(nums = [-1,1,0,-3,3])
    [0, 0, 9, 0, 0]

    """
    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        """
        Args:
            nums (List[int]): nums to calculate products from
        Returns:
            List[int]: product of all nums except self for each index

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(1)``

        :Strategy:

            if allowed division, could just find total product and divide
            by each element for each index (problem says **no division** though)

            make two passes through ``nums``, accumulating a running product for
            both directions (``left`` and ``right``)

            first traverse left to right, updating ``products`` output array
            with the left-hand accumulated product (``left``) before that point
            (*except self*), then update ``left`` with current num (*self*)
            after using it for ``products`` calculation (it will be used for
            next index)

            then traverse from right to left. ``products`` output array will
            have product of all elements excluding current index each time it
            is multiplied by right-hand accumulated product (``right``), which
            is updated **after** using it for ``products`` calculation (*except
            self*)


        """
        products = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            products[i] *= left
            # update product after above product calculation (except self)
            left *= nums[i]

        right = 1
        # go backwards
        for i in range(len(nums) - 1, -1, -1):
            # this will now have product of all elements to left and right
            products[i] *= right
            right *= nums[i]

        return products
