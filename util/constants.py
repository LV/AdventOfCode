from dataclasses import dataclass


LATEST_AOC_YEAR: int = 2024

@dataclass
class PuzzleID:
    """Class for identifying the Advent of Code puzzle"""
    year: int
    day: int
    part: int
