from util.constants import PuzzleID
import importlib
import os


def _check_if_puzzle_solution_exists(puzzle: PuzzleID) -> None:
    """Check if puzzle solution file exists before importing"""
    module_path = os.path.join("solutions", str(puzzle.year), f"{puzzle.day:02}_{puzzle.part}.py")
    if not os.path.exists(module_path):
        raise NotImplementedError(f"AoC {puzzle.year} day {puzzle.day} part {puzzle.part} has not been solved yet.")


def _check_puzzle_test_cases(puzzle: PuzzleID) -> None:
    """Checks for puzzle test case"""
    puzzle_input_test_path = os.path.join("input", str(puzzle.year), f"{puzzle.day:02}", "test_cases")
    puzzle_input_test_part_path = os.path.join(puzzle_input_test_path, f"part_{puzzle.part}")

    should_test: bool = True

    if not os.path.exists(puzzle_input_test_path):
        print(f"WARNING: Puzzle test case directory for {puzzle.year} day {puzzle.day} not found.")
        should_test = False

    if not os.path.exists(puzzle_input_test_part_path):
        print(f"WARNING: Puzzle test case directory for {puzzle.year} day {puzzle.day} part {puzzle.part} not found.")
        should_test = False

    if not os.listdir(puzzle_input_test_part_path):
        print(f"WARNING: No puzzle test case(s) found for {puzzle.year} day {puzzle.day} part {puzzle.part} were found.")
        should_test = False

    if not should_test:
        print("Skipping tests...")
        return

    print(os.listdir(puzzle_input_test_part_path))
    # TODO: Actually run test cases


def _check_puzzle_input_and_download_if_necessary(puzzle: PuzzleID) -> None:
    """Checks if the puzzle input already exists, and downloads if if it doesn't exist"""
    puzzle_input_directory = os.path.join("input", str(puzzle.year), f"{puzzle.day:02}")
    puzzle_input_text_path = os.path.join(puzzle_input_directory, "input.txt")

    if os.path.exists(puzzle_input_text_path):
        return

    os.makedirs(puzzle_input_directory, exist_ok=True)
    # TODO: Make a request for getting input
    


def run_puzzle_solve(puzzle: PuzzleID) -> Any:
    """Runs the Puzzle Solution's `solve()` function"""

    _check_if_puzzle_solution_exists(puzzle)

    solution_module = importlib.import_module(f"solutions.{puzzle.year}.{puzzle.day:02}_{puzzle.part}")

    if not hasattr(solution_module, "solve"):
        raise AttributeError(f"solutions/{puzzle.year}/{puzzle.day:02}_{puzzle.part}.py has no `solve()` function.")

    _check_puzzle_input_and_download_if_necessary(puzzle)

    return solution_module.solve()


