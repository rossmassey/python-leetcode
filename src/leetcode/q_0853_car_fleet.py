from typing import Optional, List, Dict


class Solution0853:
    """
    `Medium <https://leetcode.com/problems/car-fleet/>`_
    ----------------------------------------------------

    .. sidebar:: Constraints

        * ``n == position.length == speed.length``
        * ``1 <= n <= 10^5``
        * ``0 < target <= 10^6``
        * ``0 <= position[i] < target``
        * All the values of ``position`` are **unique**.
        * ``0 < speed[i] <= 10^6``

    There are ``n`` cars going to the same destination along a one-lane road.
    The destination is ``target`` miles away.

    You are given two integer array ``position`` and ``speed``, both of length
    ``n``, where ``position[i]`` is the position of the ``i^th`` car and
    ``speed[i]`` is the speed of the ``i^th`` car (in miles per hour).

    A car can never pass another car ahead of it, but it can catch up to it and
    drive bumper to bumper **at the same speed**. The faster car will **slow
    down** to match the slower car's speed. The distance between these two cars
    is ignored (i.e., they are assumed to have the same position).

    A **car fleet** is some non-empty set of cars driving at the same position
    and same speed. Note that a single car is also a car fleet.

    If a car catches up to a car fleet right at the destination point, it will
    still be considered as one car fleet.

    Return *the number of car fleets* that will arrive at the destination.

    ------

    :Example 1:

    >>> Solution0853.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3])
    3

    The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.

    The car starting at 0 does not catch up to any other car, so it is a fleet by itself.

    The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

    Note that no other cars meet these fleets before the destination, so the answer is 3.


    :Example 2:

    >>> Solution0853.carFleet(target = 10, position = [3], speed = [3])
    1

    There is only one car, hence there is only one fleet.


    :Example 3:

    >>> Solution0853.carFleet(target = 100, position = [0,2,4], speed = [4,2,1])
    1

    The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.

    Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.

    """

    @staticmethod
    def carFleet(target: int, position: List[int], speed: List[int]) -> int:
        """
        Args:
            target (int): ending position
            position (List[int]): car starting positions
            speed (List[int]): car starting speeds
        Returns:
            int: number of car fleets

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            ``sort`` the cars by descending position, starting with closest to
            destination

            use a ``stack`` to track the arrival times of each car

            if a car starting further away has an earlier arrival time than any
            on the stack (which start closer), then they meet at some point to
            become a single car fleet

            so ``pop`` from ``stack`` any time the top of ``stack`` arrival time is
            less than or equal to next item on ``stack`` (want to maintain a
            monotonic increasing stack)

            return number of items in stack at the end (which will be all the
            merged arrival times)

        """
        stack = []

        # sort in descending position to destination (start with closest)
        for car_start, car_speed in sorted(zip(position, speed), reverse=True):
            stack.append((target - car_start) / car_speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

    @staticmethod
    def carFleetClearer(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Args:
            target (int): ending position
            position (List[int]): car starting positions
            speed (List[int]): car starting speeds
        Returns:
            int: number of car fleets

        ------

        :Runtime:   ``O(n)``
        :Space:     ``O(n)``

        :Strategy:

            this has similar logic to one above, but sorts in ascending order

            for each car, calculate the ``arrival_time``

            compare to items on the stack, if a later car's ``arrival_time``
            is greater than the top of stack, than it will catch up to one
            at top.

            ``pop`` so it is counted as single merged car fleet

            return number of items in stack at end

            this is slightly less efficient due to the while loop and extra
            stack operations, but easier to undertstand

        """
        stack = []

        # sort in ascending position to destination
        for car_start, car_speed in sorted(zip(position, speed)):
            arrival_time = (target - car_start) / car_speed

            while stack and arrival_time >= stack[-1]:
                stack.pop()

            stack.append(arrival_time)

        return len(stack)
