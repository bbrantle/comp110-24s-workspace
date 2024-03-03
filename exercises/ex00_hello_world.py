"""My first exercise in CAMP110!"""

__author__ = "730657739"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "Hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("what is your name? ")))
