#!/usr/bin/python
# -*- coding: utf-8 -*-

# built-in imports
import contextlib
import pathlib

# third-party imports
from rich import print


# path to the dictionary file
DICT = pathlib.Path("hunspell-en_US.dic")


def chunks(source_list: list, chunk_size: int):
    """https://stackoverflow.com/a/312464"""
    for i in range(0, len(source_list), chunk_size):
        yield source_list[i : i + chunk_size]


def read_dict(path: pathlib.Path) -> list:
    with open(path, "r") as dictionary:
        return [w.strip().lower() for w in dictionary.readlines()]


def solve():
    words = read_dict(DICT)

    # find a word with 5 different chars as the initial guess
    print("If the initial word is not in the word list, press enter for the next guess")
    print("Otherwise press ^C to continue")
    with contextlib.suppress(KeyboardInterrupt):
        for word in words:
            if len(set(word)) == 5:
                print(f"Initial guess: {word}")
                input()
    print("\n")

    includes = []
    excludes = []

    while True:
        guessed_word = input("Guessed word: ")

        while True:
            try:
                result = input("Input guess result (word[char],position[int],correct[int]): ")
                if result == "":
                    for c in guessed_word:
                        for i in includes:
                            if c == i[0]:
                                break
                        else:
                            if c not in excludes:
                                excludes.append(c)
                    break
                includes.append(
                    tuple(
                        [
                            result.split(",")[0],
                            int(result.split(",")[1]),
                            int(result.split(",")[2]),
                        ]
                    )
                )
            except (IndexError, ValueError):
                print("Invalid input")

        possible = []
        for word in words:

            for c in excludes:
                if c in word:
                    continue

            for guess in includes:
                if guess[2] == 1:
                    if word[guess[1]] != guess[0]:
                        break
                else:
                    if guess[0] not in word or word[guess[1]] == guess[0]:
                        break
            else:
                possible.append(word)

        print("Possible answer (s): ")
        for c in chunks(possible, 10):
            print(c)


if __name__ == "__main__":
    solve()
