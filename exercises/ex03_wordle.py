"""Implements the game Wordle"""

__author__: str = "730657739"


def contains_char(word: str, letter: str) -> bool:
    """Determines whether a letter is in the target word"""
    assert len(letter) == 1, f"'{letter}') is not 1"
    i: int = 0
    while word[i] != letter:
        i = i + 1
        if i > len(word) - 1:
            return False
    return True


def emojified(guess: str, secret: str) -> str:
    """codifies the results of a Wordle guess"""
    assert len(guess) == len(secret)
    "Guess must be same length as secret"
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    answer: str = ""
    while i < len(guess):
        if contains_char(word=secret, letter=guess[i]) is False:
            i = i + 1
            answer = answer + WHITE_BOX
            # concatenates answer with white box in the right order (same for other colors)
        elif guess[i] == secret[i]:
            i = i + 1
            answer = answer + GREEN_BOX
        else:
            i = i + 1
            answer = answer + YELLOW_BOX

    return answer


def input_guess(length: int) -> str:
    """Ask a user for a guess of an expected length"""
    answer = input(f"Enter a {length} character word:")
    while len(answer) != length:
        answer = input(f"That wasn't {length} chars! Try again:")
    return str(answer)


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    # secret word "codes"
    i: int = 1
    while i <= 6:
        print(f"=== Turn {i}/6 ===")
        guess: str = input_guess(length=len(secret))
        print(emojified(guess=guess, secret=secret))
        if guess != secret:
            i = i + 1
        # if guess = secret print winning phrase
        else:
            print(f"You won in {i}/6 turns!")
            return None
    print("X/6 - Sorry, try again tomorrow!")
    return None


if __name__ == "__main__":
    main(secret="codes")
