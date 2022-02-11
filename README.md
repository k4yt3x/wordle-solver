# Wordle Solver

A small script to help me solve Wordle because I'm that lazy.

Warning: I didn't write this to be efficient nor elegant at all, so you'll probably have a hard time with the UI and the untidy code. I just thought I might as well save it to GitHub.

![demo](https://user-images.githubusercontent.com/21986859/153531757-d3081d3a-d8b2-4215-b5aa-4c03dbbfaab1.png)

## Usages

Clone/download the repo:

```shell
git clone https://github.com/k4yt3x/wordle-solver.git
cd wordle-solver/src
```

Install dependencies:

```shell
pip3 install -U -r requirements.txt
```

Launch the script:

```shell
python3 wordle_solver.py
```

1. The script will give you an initial guess. If this word exists in Wordle, press ^C to continue. Otherwise, press enter to get the next initial word.
1. Pick a word from the possible answers, and tell the script what you picked.
1. Tell the script which characters exist in the word and where. See the notes below.
1. Goto step 2 unless you've found the right answer, then ^C.

More about how to do step 3:

- The format is char[CHAR],position[INT],correct[INT]
  - char: the character that exists or is in the right position
  - position: the position you put it at (index start at 0)
  - correct: 1 if it's in the right position, else 0
- For example, if you put character `c` at index 1 but it's not at the right place, input `c,1,0`
- If `x` is at the right place at index 4, input `x,4,1`
- You must enter the result for all characters that exist in the last word you put in. The program will automatically list all character not entered as excluded.
- When you're done, press enter blank input to continue
