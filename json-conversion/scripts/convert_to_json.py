# convert_to_json.py

from pathlib import Path
import json

def parse_entries():
    """
    Reads the dictionary file and groups the lines for each term.
    """
    # separate terms
      # 1. open + read domislang.txt
      # 2. loop through lines
      # 3. group the lines for each term into a list
      # 4. return a list of these lists

    script_dir = Path(__file__).parent

    file_path = script_dir.parent / "vocab" / "domislang.txt"

    print(f"Attempting to open file at: {file_path}")

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            all_lines = file.readlines()

    except FileNotFoundError:
        print(f"ERROR: Could not find the file at the specified path: {file_path}")
        return []

    print(f"Successfully read {len(all_lines)} lines from the file.")

    # Next step: "chunk" this list.

    # The first 20 lines to confirm it works
    print("\n--- First 20 lines ---")
    for line in all_lines[:20]:
        print(line.strip())

    return all_lines


if __name__ == "__main__":
    lines = parse_entries()