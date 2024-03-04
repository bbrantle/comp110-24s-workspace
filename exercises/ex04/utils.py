"""Implement functions skeletons for utils"""

__author__: str = "730657739"


def only_evens(list_all: list[int]) -> list[int]:
    """Given a list, returns the even values of the list"""
    i: int = 0
    evens: list[int] = []
    while i < len(list_all):
        if list_all[i] % 2 == 0:
            evens.append(list_all[i])
            i = i + 1
        else:
            i = i + 1
    return evens
