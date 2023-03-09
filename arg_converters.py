import re
from pathlib import Path
import glob


def convert_to_path(path: str) -> Path:
    if path.startswith('~'):
        path = Path(path).expanduser()
    else:
        path = Path(path).absolute()

    is_glob_dir = glob.has_magic(str(path))
    is_dir_exists = path.exists()
    
    if is_glob_dir and not is_dir_exists:
        return [Path(path) for path in glob.iglob(str(path))]
    elif is_dir_exists and path.is_dir():
        return [path]
    raise ValueError("Path does not exist or not a directory!")

def flatten_paths(paths:list[list[Path]|Path]) -> list[Path]:
    flatten = []
    for path in paths:
        if isinstance(path, Path):
            flatten.append(path)
        else:
            flatten.extend(path)
    return flatten

def convert_to_regular_expression(regular_expression: str) -> re.Pattern:
    try:
        regular_expression = re.compile(regular_expression)
        return regular_expression
    except Exception as e:
        print("Regex pattern: ", e)
        raise ValueError("Invalid regex pattern")


def convert_list_to_set(strings: list[str]) -> set[str]:
    return set(strings)
