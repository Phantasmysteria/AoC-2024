import typing
import itertools

# Quick way to convert input file into list of lines
def listLines(day: str, part: str) -> list[str]:
    with open(f"inputD{day}P{part}.txt", "r") as f:
        return [item.rstrip() for item in f.readlines()]

# Quick way to convert input file into list of list of lines separated by delimiter
def listLinesWithGroup(day: str, part: str, groupSep: str) -> list[str]:
    with open(f"inputD{day}P{part}.txt", "r") as f:
        return [list(group) for key, group in itertools.groupby([item.rstrip() for item in f.readlines()], lambda x: x == groupSep) if not key]
    
if __name__ == '__main__':
    print("Why are you running this file?")