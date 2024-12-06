import argparse
from .constants import LATEST_AOC_YEAR, PuzzleID


def _get_year_number(value: str) -> int:
    """Validates the year number"""
    ivalue = int(value)
    if not 2015 <= ivalue <= LATEST_AOC_YEAR:
        raise argparse.ArgumentTypeError(f"Year must be between 2015 and {LATEST_AOC_YEAR} inclusive, got {value}")
    return ivalue


def _get_day_number(value: str) -> int:
    """Validates the day number"""
    ivalue = int(value)
    if not 1 <= ivalue <= 25:
        raise argparse.ArgumentTypeError(f"Day number must be between 1 and 25 inclusive, got {value}")
    return ivalue


def _get_part_number(value: str) -> int:
    """Validates the part number"""
    ivalue = int(value)
    if ivalue != 1 and ivalue != 2:
        raise argparse.ArgumentTypeError(f"Part number must be 1 or 2, got {value}")
    return ivalue


def get_puzzle_id_from_argparse() -> PuzzleID:
    """Returns a valid PuzzleID from ArgParse"""
    parser = argparse.ArgumentParser(
        prog="Advent of Code 2024",
        description="My solutions for Advent of Code 2024",
        epilog="Made by Luis Victoria",
    )

    _ = parser.add_argument('-y', '--year', type=_get_year_number, required=True, help=f"Year; between 2015 and {LATEST_AOC_YEAR} inclusive")
    _ = parser.add_argument('-d', '--day', type=_get_day_number, required=True, help="Day number; between 1 and 25 inclusive")
    _ = parser.add_argument('-p', '--part', type=_get_part_number, required=True, help="Part number; should be 1 or 2")

    args = parser.parse_args()
    return PuzzleID(year=args.year, day=args.day, part=args.part)
