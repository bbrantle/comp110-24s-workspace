"""A countdown program..."""


def main() -> None:
    seconds: int = int(input("How many seconds?"))
    countdown(seconds)
    print(f"Main {seconds}")


def countdown(seconds: int) -> None:
    print("T minus")
    while seconds > 0:
        print(seconds)
        seconds = seconds - 1

    print(f"countdown {seconds}")


if __name__ == "__main__":
    main()
