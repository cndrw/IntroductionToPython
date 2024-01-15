import argparse
from pathlib import Path


def get_number_lines_for_files(root_dir):
    for filepath in root_dir.glob("*.txt"):
        with open(filepath, mode='r') as file:
            num_lines = len(file.readlines())
            print(f"File {filepath} has {num_lines} lines.")


# parser = argparse.ArgumentParser()
# parser.add_argument("--file-dir", type=str, default=str(Path(__file__).parent))
# args = parser.parse_args()
# root_dir = Path(args.file_dir)
# get_number_lines_for_files(root_dir)
print(__file__)