import re
from pathlib import Path
from collections import Counter

def report_on_data_integrity():
    """
    Reads the dictionary file and reports on data integrity, checking for
    duplicate numbers, skipped numbers, and duplicate terms.
    """
    try:
        script_dir = Path.cwd()
        file_path = script_dir / "output" / "domislang_renumbered.txt"
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ ERROR: Could not find 'domislang_renumbered.txt' at {file_path}")
        return

    print("--- Analyzing data integrity in domislang_renumbered.txt ---")

    found_numbers = []
    terms_to_lines_map = {}

    for line in lines:
        # Entries with or without a hyphen.
        match = re.search(r'^(\d+)\.\s(.+?)\s*(?: - |$)', line)

        if match:
            number = int(match.group(1))
            term = match.group(2).strip()
            original_line = line.strip()

            found_numbers.append(number)

            if term not in terms_to_lines_map:
                terms_to_lines_map[term] = [original_line]
            else:
                terms_to_lines_map[term].append(original_line)

    if not found_numbers:
        print("No entries were found in the file.")
        return

    # (The rest of the script is unchanged as the logic was correct)
    number_counts = Counter(found_numbers)
    duplicate_numbers = [num for num, count in number_counts.items() if count > 1]
    expected_range = set(range(1, max(found_numbers) + 1))
    actual_numbers = set(found_numbers)
    skipped_numbers = sorted(list(expected_range - actual_numbers))

    print(f"\nAnalysis complete. Found {len(found_numbers)} total entry markers.")
    has_errors = False

    if duplicate_numbers:
        has_errors = True
        print("\n❌ Found DUPLICATE entry numbers:")
        print(f"   {duplicate_numbers}")

    if skipped_numbers:
        has_errors = True
        print("\n❌ Found SKIPPED numbers (missing from the sequence):")
        print(f"   {skipped_numbers}")

    duplicate_term_entries = {term: lines for term, lines in terms_to_lines_map.items() if len(lines) > 1}

    if duplicate_term_entries:
        has_errors = True
        print("\n❌ Found DUPLICATE terms:")
        for term, original_lines in duplicate_term_entries.items():
            print(f"\n  Term '{term}' was found {len(original_lines)} times in these entries:")
            for line in original_lines:
                print(f"    - {line}")

    if not has_errors:
        print("\n✅ Success! No data integrity issues were found.")


if __name__ == "__main__":
    report_on_data_integrity()