#!/usr/bin/python3
"""
    Given a list of non-negative integers representing the heights of walls
    with unit width 1,
    as if viewing the cross-section of a relief map,
    calculate how many square units of water will be retained after it rains.
"""


def rain(walls):
    """Defines the rain function"""

    water = 0

    # Check if there are at least three walls or the list is empty
    if len(walls) < 3 or not walls:
        return 0

    # Iterate over each wall in the middle
    for i in range(1, len(walls) - 1):
        # Calculate the maximum height of the wall on the left side
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])

        # Calculate the maximum height of the wall on the right side
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])

        # Calculate the amount of water retained above the current wall
        water += min(left, right) - walls[i]

    return water
