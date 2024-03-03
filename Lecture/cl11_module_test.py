"""Test for the count function"""

from Lecture.cl11_module import count

# Example / Expected Function Calls


# count ([1, 2, 3], 4) == 0
def test_count_no_occurences() -> None:
    assert count([1, 2, 3], 4) == 0


def test_count_one_occurence() -> None:
    assert count([1, 2, 3], 1) == 1


# count ([1, 2, 3], 1) == 1
# count ([1, 2, 1], 1) == 2


def test_many_occurences() -> None:
    assert count([1, 1, 1], 1) == 3


# Edge Cases

# count([], 1) == 0


def test_count_empty_list() -> None:
    assert count([], 1) == 0
