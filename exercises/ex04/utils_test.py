"""Tests for the util functions """

__author__: str = "730657739"

from exercises.ex04.utils import only_evens


# use cases
def test_only_evens_first_number() -> None:
    """Tests only_evens when the first number is even only"""
    assert only_evens([2, 5, 11]) == [2]


def test_only_evens_alternating() -> None:
    """Test only_evens when there are even and odd numbers alternating"""
    assert only_evens([2, 3, 4, 5]) == [2, 4]


# edge case
def test_only_evens_empty_list() -> None:
    """Test only_evens when given an empty list"""
    assert only_evens([]) == []
