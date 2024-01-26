"""A program to determine the amount of supplies needed for a tea party"""

__author__: str = "730657739"


def main_planner(guests: int) -> None:
    """entrypoint to the tea party program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=(treats(people=guests)))
        )
    )


def tea_bags(people: int) -> int:
    """A function to calculate the number of tea bags needed"""
    return people * 2


def treats(people: int) -> int:
    """A function to calculate the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """A function to calculate the cost of a tea party"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
