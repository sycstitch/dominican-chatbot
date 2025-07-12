### Task: Automating JSON Conversion

#### Key Learnings & Decisions:

* **Problem: `FileNotFoundError` with Relative Paths**
    * A script's relative paths (e.g., `../file.txt`) are based on the *current working directory* (where the `python` command is run), not the script's own location. This makes the script brittle.
    * **Solution:** Use Python's `pathlib` library to create robust, absolute paths. By starting with `Path(__file__).parent`, the script can always locate adjacent files and folders, regardless of where it's executed from.

* **Best Practices for Opening Files**
    * Always use a `with open(...)` block. This is safer because it automatically handles closing the file, even if errors occur during processing.
    * Specify `encoding="utf-8"` when opening text files, especially those with special characters (like accents or `ñ`), to prevent `UnicodeDecodeError`.

* **Virtual Environments (`venv`) vs. Docker**
    * Even when using Docker for the final application, a local `venv` is a best practice.
    * **Docker:** Isolates the *running application's* environment.
    * **`venv`**: Isolates the *local development* environment. This ensures tools like code linters, formatters, and debuggers in the code editor work correctly and consistently with the project's dependencies (`requirements.txt`).

---

### 🧠 Concept Table for Your Dominican Slang Parser Project

| **Concept**                                               | **Why You Should Learn It**                                                   | **What Part of the Project It Helps With**                            |
| --------------------------------------------------------- | ----------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| **File I/O** (`open`, `with`, `readline`)                 | Safely reading files line-by-line without crashes                             | Reading and loading the `domislang.txt` source file                   |
| **String Methods** (`strip`, `split`, `startswith`, etc.) | Trimming and dissecting text cleanly                                          | Parsing lines like `Usage: 7/10`, `SYN: ...`, or examples             |
| **List Basics + List Comprehensions**                     | Building and transforming sequences of entries                                | Storing grouped lines per term, synonyms, entries                     |
| **Dictionaries & Nesting**                                | Storing complex structured data in JSON-ready format                          | Building `meanings`, `tags`, `etymology`, etc.                        |
| **Control Flow** (`for`, `while`, `if`, `break`)          | Directing how your script reacts to each line                                 | Deciding whether to start a new term, skip a line, extract a field    |
| **Returning Values from Functions**                       | Getting processed data back after parsing                                     | Returning lists of entries, counts, or structured data                |
| **Counting Lists** (e.g., `len(entries)`)                 | Verifying if the right number of terms were parsed                            | `print(f"{len(entries)} entries parsed")` sanity checks               |
| **Skipping Lines or Characters**                          | Ignoring junk lines like `# A` or lines that don't match your expected format | Keeping your output clean from section headers or typos               |
| **Regex (Regular Expressions)**                           | Matching complex patterns, e.g., multi-term lines or `7/10` usage formats     | Parsing usage, spotting combined terms like `Fullín / Fundillo / Fuí` |
| **JSON Serialization** (`json.dump`, `json.dumps`)        | Writing your final output to `.json` in a structured way                      | Exporting the cleaned data to use in your app                         |
| **Error Handling** (`try/except`)                         | Avoiding crashes on missing fields or bad lines                               | Handling broken or malformed entries gracefully                       |
| **Custom Parsing Logic**                                  | Chaining together parsing steps, organizing logic clearly                     | Turning a chunk of lines into one JSON object                         |
| **Schema Design (Core vs Specialist Keys)**               | Enforcing consistency and cleanliness in data shape                           | Making sure every entry has `term`, `tags`, `meanings`, etc.          |
| **Data Normalization**                                    | Standardizing terms and tags (e.g., lowercase, removing accents)              | Making your data easier to search, compare, and match                 |
| **Data Cleaning Best Practices**                          | Dealing with typos, extra whitespace, or inconsistent formats                 | Ensuring cleaner output and fewer bugs down the line                  |
| **Unit Testing with `pytest`**                            | Writing automated tests to make sure your parsing logic works                 | Validating that each raw entry produces the right JSON                |
| **Text Preprocessing Pipelines**                          | Separating parsing into clear, testable steps                                 | Scaling your script as logic becomes more complex                     |
| **Splitting Multiple Terms into Separate Objects**        | Following your "One Term, One Object" rule                                    | Handling entries like `fullín / fundillo / fuí` correctly             |
| **Working with Optional Fields**                          | Avoiding empty or irrelevant keys (e.g., no `etymology` unless needed)        | Keeping your JSON file clean and minimal                              |
| **Validating Output** (`assert`, type checking)           | Ensuring every object meets your schema                                       | Catching bugs before saving/exporting to JSON                         |

---

### Roadmap

#### **Step 1: Read the File and Confirm Path**

First, let's just make sure we can access and read the source file. This step validates your file path and environment setup.

* **What to Do:** In a new cell, write code to open `domislang.txt` and print the first 500 characters. This confirms you're reading the correct file without overwhelming your screen.
* **Python Concepts:**
    * **`os.path.join()`**: For building operating-system-aware file paths.
    * **`with open(...) as f:`**: The standard, safe way to open and automatically close a file.
    * **`f.read(500)`**: Reads a specified number of characters from the file.

---

#### **Step 2: Split the File into Individual Entries**

Now, let's break that single block of text into a list, where each item is a complete dictionary entry.

* **What to Do:** Read the entire file and split it into a list of strings based on blank lines between entries. Print the total number of entries you've found and inspect the first two items in the list to see if they were separated correctly.
* **Python Concepts:**
    * **`string.read()`**: To read the entire contents of the file into a string.
    * **`re.split()`**: A powerful function from the regular expression module. Using `re.split(r'\n\s*\n', content)` will split the text on any occurrence of one or more blank lines.
    * **`len()`**: To count the number of items in your list.
    * **List Indexing (`my_list[0]`)**: To access and inspect specific elements.

---

#### **Step 3: Parse a Single, Simple Entry**

Instead of trying to parse everything at once, focus on making one simple case work perfectly. We'll use the `abimbao` entry as our test case.

* **What to Do:** Create a function named `parse_simple_entry(text)`. Inside, use regex to extract only three things: the term (`abimbao`), the short definition (`beaten up`), and the usage score (`8`). Have the function return a dictionary with these values and print the result.
* **Python Concepts:**
    * **Function Definition (`def`)**: To create a reusable block of code.
    * **`re.search()`**: To find the first occurrence of a pattern in a string.
    * **Regex Groups (`()`)**: To capture specific parts of the matched pattern.
    * **Dictionaries**: To store the extracted data in a `key: value` format.

---

#### **Step 4: Expand Parser for Key-Value Fields**

Build on the simple parser to extract all the single-line fields (`EX:`, `GS:`, `EN:`, `SYN:`).

* **What to Do:** Modify your function, renaming it to `parse_entry(text)`. Add a regular expression that finds all key-value pairs. Test it again with the `abimbao` text and print the resulting, more detailed dictionary.
* **Python Concepts:**
    * **`re.findall()`**: To find *all* occurrences of a pattern.
    * **`re.MULTILINE`**: A flag that allows your pattern to match at the beginning of each line, not just the start of the string.
    * **Dictionary Updates**: Adding new key-value pairs to the dictionary you created in the last step.

---

#### **Step 5: Handle Grouped Terms (The "One Term, One Object" Rule)**

Now, tackle the first major business rule from your documentation. The goal is to handle entries like `Fullín / Fundillo / Fuí`.

* **What to Do:** Modify `parse_entry` to check if the term contains a `/`. If it does, split the terms and make the function return a **list of dictionaries**—one for each term. Test this specifically with the `fullín` entry text and confirm the output is a list containing three distinct objects.
* **Python Concepts:**
    * **`string.split('/')`**: To split the header line into a list of term names.
    * **`for` Loops**: To iterate over the list of term names and create a dictionary for each one.
    * **Returning a List**: Changing the function's output from a single dictionary to a list of dictionaries.

---

#### **Step 6: Handle Specialist Keys (Etymology)**

Let's add logic for another specific rule: capturing etymology when it's present.

* **What to Do:** Add code to `parse_entry` that looks for the `History:` and `Original word:` fields. If found, create a nested `etymology` dictionary and add it to the main object. Because the etymology only applies to `fullín`, make sure it's only added to the *first* object in the list your function returns.
* **Python Concepts:**
    * **Conditional Logic (`if`)**: To check if the `History:` field was found.
    * **Nested Dictionaries**: Creating a dictionary inside another dictionary.

---

#### **Step 7: Full Integration, Validation, and Saving**

You're ready for the final step! Run your completed parser over all the entries and save the result.

* **What to Do:**
    1.  Create an empty list called `all_parsed_terms`.
    2.  Loop through the `raw_entries` list from Step 2.
    3.  In the loop, call your final `parse_entry` function for each entry and use `list.extend()` to add the returned dictionary (or dictionaries) to `all_parsed_terms`.
    4.  Print the final total number of objects created.
    5.  Run the validation script logic from the previous answer to check your final list.
    6.  Save the `all_parsed_terms` list to `dominican-terms-WIP.json`.
* **Python Concepts:**
    * **`list.extend()`**: To add all items from one list to another (crucial because `parse_entry` can return a list).
    * **`json.dump()`**: To serialize your Python list of dictionaries into a JSON formatted file on disk.