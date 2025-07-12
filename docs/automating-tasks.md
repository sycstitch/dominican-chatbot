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

Perfect — here’s a personalized study plan based on your project and where you're at. It's broken into 3 phases:

🧩 PHASE 1: Get the Core Working
Goal: Read the file, split it into entries, and output clean data.
🔹 Concepts to Study (in order)
	1	File I/O Basics
	- open(), with statement, reading lines
	- ✅ Why: You'll read domislang.txt line by line.
	2	String Methods
	- .strip(), .split(), .startswith(), .lower()
	- ✅ Why: Used constantly when parsing lines like EX: ..., Usage: ..., SYN: ...
	3	Lists
	- How to build lists, append to them, loop through them
	- ✅ Why: Each term = a list of lines → list of lists
	4	Control Flow
	- for loops, if/elif, break, continue
	- ✅ Why: You’ll use this to build chunks, skip headers (# A), or exit early
	5	Returning Values from Functions
	- return keyword, returning lists and dicts
	- ✅ Why: Your parse_entries() function needs to return structured data
	6	Basic Counting and Lengths
	- len(), print() for sanity checking
	- ✅ Why: You want to print how many terms were parsed

🏗 PHASE 2: Build the Schema
Goal: Convert each entry chunk into a JSON-ready object that matches your format.
🔹 Concepts to Study (in order)
	7	Dictionaries & Nesting
	- Creating dicts, nesting dicts in lists
	- ✅ Why: You’re building deeply nested objects for each term and its meanings
	8	Working with Optional Keys
	- Conditional logic to add fields only when needed
	- ✅ Why: You don’t want empty etymology keys in every object
	9	String Cleaning + Normalization
	- Replacing accents, trimming, standardizing terms/tags
	- ✅ Why: Ensures consistency (bembú, Bembú, BEMBÚ → all normalized)
	10	Skipping Unwanted Lines
	- Using .startswith('#') or regex to skip headers
	- ✅ Why: Some lines like # A or separators are junk
	11	Regex Basics
	- re.match(), re.search(), capturing groups
	- ✅ Why: Needed for multi-term lines like Fullín / Fundillo / Fuí, or matching Usage: 7 / 10
	12	JSON Serialization
	- json.dump() vs json.dumps(), handling Unicode, indent=2
	- ✅ Why: You’ll be exporting your final file

🧪 PHASE 3: Clean It, Test It, Expand It
Goal: Ensure accuracy, clean edge cases, and prepare to scale the project.
🔹 Concepts to Study (in order)
	13	Data Cleaning Best Practices
	- Standardizing tags, trimming weird whitespace, fixing typos
	- ✅ Why: Cleaner output = easier use later
	14	Unit Testing with Pytest
	- Writing tests for parse_chunk(), parse_usage(), etc.
	- ✅ Why: Catches bugs when entries are malformed or incomplete
	15	Data Validation & Schema Enforcement
	- Using assert, manually checking fields
	- ✅ Why: Keeps entries consistent (e.g., every term should have usage, even if 0)
	16	Splitting Grouped Terms
	- Logic to take "Fullín / Fundillo / Fuí" and create 3 entries
	- ✅ Why: This enforces your "One Term, One Object" rule
	17	Text Preprocessing Pipelines (Optional)
	- Breaking your parsing into reusable, testable chunks
	- ✅ Why: Makes your code modular and easy to test/extend

📌 Suggested Tools Alongside
	- Python Tutor — to visualize loops and function returns
	- replit or a notebook — for testing small snippets interactively
	- Your own test_cases/ folder with raw text examples to try during testing