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