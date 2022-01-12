from simple_chalk import chalk
from typing import List
import random
import requests


def get_word_list() -> List[str]:
    resp = requests.get(
        "https://raw.githubusercontent.com/sastrawi/sastrawi/master/data/kata-dasar.txt"
    )
    words = resp.text.split("\n")
    return list(filter(lambda x: len(x) == 5, words))


def sample(word_list: List[str]) -> str:
    return random.choice(word_list)


def check(word: str, ref_word: str) -> str:
    marks = []
    for letter, ref_letter in zip(word, ref_word):
        if letter == ref_letter:
            marks.append(chalk.green("O"))
        elif letter in ref_word:
            marks.append(chalk.yellow("o"))
        else:
            marks.append(chalk.red("X"))
    return "".join(marks)


def main():
    five_letter_words = get_word_list()
    ref_word = sample(five_letter_words)
    n_tries = 6
    marks = []
    i = 0
    while i < n_tries:
        print(f"#{i+1}/{n_tries}")
        guess = str(input()).strip().lower()
        if guess not in set(five_letter_words):
            continue
        mark = check(guess, ref_word)
        print(mark)
        marks.append(mark)
        if mark == chalk.green("O") * 5:
            break
        i += 1
    print(chalk.blue("====="))
    for mark in marks:
        print(mark)
    print(ref_word)


if __name__ == "__main__":
    main()