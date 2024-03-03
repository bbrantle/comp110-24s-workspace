"""8-Ball GPT"""

from random import random

RESPONSES: tuple[str, ...] = (
    "most Certainly",
    "ask again later",
    "Signs point to yes",
    "Absolutely not",
)


def random_choice(choices: tuple[str, ...]) -> str:
    """Return one random str from atuple of strs."""
    return choices[random_index(upper_bound=len(choices))]


def random_index(upper_bound: int) -> int:
    """Return an int between [0, upper_bound] not inclusive of upper bound"""
    # Return a single expression that :
    # 1. Multiplies random () by upper_bound
    # 2. Converts the result into an integer
    # 3. Hint: nested function call expression
    return int(random() * upper_bound)


def random_branch() -> str:
    """Return a random response"""
    RESPONSE: int = random_index(3)
    if RESPONSE == 0:
        return "Most Certainly"
    elif RESPONSE == 1:
        return "Ask again later"
    else:
        return "Not a chance"


if __name__ == "__main__":
    input("Ask a yes no question")
    print(random_choice(RESPONSES))
