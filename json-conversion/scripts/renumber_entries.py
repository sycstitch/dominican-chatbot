import re
from pathlib import Path

def renumber_file_entries():
    """
    Reads the dictionary file and writes a new file with sequentially
    numbered entries using an optimized replacement method.
    """
    try:
        # Define paths
        script_dir = Path.cwd()
        source_file_path = script_dir.parent / "vocab" / "domislang.txt"
        output_file_path = script_dir / "output" / "domislang_renumbered.txt"

        with open(source_file_path, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()

    except FileNotFoundError:
        print(f"❌ ERROR: Could not find 'domislang.txt'. Please ensure it's in the vocab folder.")
        return

    new_lines = []
    entry_counter = 1

    print("--- Starting re-numbering process ---")

    for line in lines:
        # This pattern finds one or more digits at the start of the line
        pattern = r'^\d+'

        # Check if the line matches an entry start
        if re.search(pattern, line):
            # Use re.sub() to replace the matched number with the new counter
            # The '1' argument ensures it only performs one replacement per line
            new_line = re.sub(pattern, str(entry_counter), line, 1)
            new_lines.append(new_line)
            entry_counter += 1
        else:
            # It's not an entry line, so just add it as-is
            new_lines.append(line)

    # Write the re-numbered content to a new file
    try:
        with open(output_file_path, "w", encoding="utf-8") as f:
            # Using writelines is slightly more efficient than joining and writing
            f.writelines(new_lines)
        print(f"\n✅ Success! Re-numbered file created at: {output_file_path}")
        print(f"   Total entries written: {entry_counter - 1}")
    except Exception as e:
        print(f"❌ ERROR: Could not write the new file. Reason: {e}")


if __name__ == "__main__":
    renumber_file_entries()