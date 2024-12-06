from util.argparse import get_puzzle_id_from_argparse
from util.constants import PuzzleID
from util.solution_module import run_puzzle_solve

def main():
    """Program startpoint"""

    puzzle_id: PuzzleID = get_puzzle_id_from_argparse()
    print(run_puzzle_solve(puzzle_id))


if __name__ == "__main__":
    main()
