# txt-file-management-cli

A command-line Python utility for managing `.txt` files in a directory. This script provides an interactive interface that allows users to easily perform tasks such as creating, reading, writing, renaming, appending, and deleting `.txt` files, all from the terminal.

## Features

- **List all `.txt` files** in a directory in a tabular format.
- **Create new `.txt` files** easily.
- **Read the content** of existing `.txt` files.
- **Overwrite or append** content to files.
- **Rename files**, with the option to overwrite or append content.
- **Empty file contents** without deleting the file.
- **Delete `.txt` files** permanently.
- Interactive prompts to guide users through each action.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/txt-file-management-cli.git
   ```

2. Navigate to the project directory:
   ```bash
   cd txt-file-management-cli
   ```

3. Ensure you have Python 3.x installed on your machine.

4. Install the required library:
   ```bash
   pip install tabulate
   ```

## Usage

1. Run the script:
   ```bash
   python file-management.py
   ```

2. Follow the prompts to interact with `.txt` files in the current directory. Available operations include:
   - `read`: Display the content of a `.txt` file.
   - `rename`: Change the file’s name.
   - `append`: Add content to an existing file.
   - `write`: Overwrite the content of a file.
   - `empty`: Clear all content from a file without deleting it.
   - `delete`: Remove a `.txt` file from the directory.

3. Use the file listing feature to quickly see all `.txt` files in the directory.

## Example

```bash
$ python file-management.py
Found the following .txt files:
1. notes.txt
2. todo.txt

Choose an operation:
1. Read file
2. Write file
3. Append to file
4. Rename file
5. Empty file
6. Delete file
...
```
