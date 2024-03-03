"""Implement a count algorithm"""


def count(haystack: list[int], needle: int) -> int:
    """Count the occurences of needle in haystack"""
    # How do we implement count?
    # iterate through each index and count
    # if that index is equal to needle
    # return final count
    # 1. establish an index variable at 0
    idx: int = 0
    # 2. establish a tally variable
    tally: int = 0
    # 3. loop through each index
    while idx < len(haystack):
        if haystack[idx] == needle:
            tally = tally + 1

        idx = idx + 1
    return tally
