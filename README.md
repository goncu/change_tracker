# Change Tracker

**Video Link**:

## Introduction

Change Tracker is a Python command-line program utility designed to compare two XLIFF (XML-based bilingual files used in localization) files: one containing the original translation and the other containing an edited translation. The program generates an HTML report that shows the differences between two translations. The changes are displayed segment by segment; deletions are shown in red and with strikethrough, additions are shown in green. It is useful for seeing at a glance the changes made in a given translation.

## Features

**Compare original and edited translations**: The program compares two XLIFF files, extracting the source (original) and target (translated) texts from them.

**HTML report generation**: The differences between the translations are displayed in an HTML table format. Each translation segment is displayed alongside the source text and with the changes highlighted.

**Command-line interface**: The utility accepts two command-line arguments: the paths to the original and edited translation files.

**XLIFF support**: At the moment, only XLIFF files are supported.

## Program Workflow

### Step 1: Input Validation

The program validates the provided file paths using the `check_input` function. It checks that:

- The files exist at the specified paths.
- Both files have the .xliff extension.
- If any validation fails, an appropriate error message is displayed, and the program exits.

### Step 2: Extracting Text

The program then extracts source and target texts from both the original and edited XLIFF files using the `extract_text` function. This function:

- Parses the XLIFF files using Python's xml.etree.ElementTree library.
- Extracts all `<trans-unit>` elements, which contain the source and target text.
- Stores the extracted text in a list of dictionaries, where each dictionary contains a `source` key for the original text and a `target` key for the translated text.

### Step 3: Comparing Translations

After extracting the text, the program compares the original and edited translations using the `generate_report` function. The function:

- Checks if the source segments in the original and edited files are identical. If they do not match, the program exits with an error message.
- Uses redlines library to track changes between the original and edited translations.
- Writes the changes, along with the source, into an HTML file (changes.html).

### Step 4: HTML Report Generation

The HTML report is generated in a table format, with two columns:

- Source: Original source text.
- Translation: Translation with any changes between original and edited translation highlighted.

#### Example:

![changes report](/asset/table.png)

## Requirements

Before using this program, ensure that Python is installed on your system along with the required dependencies. The following libraries are necessary:

**argparse**: Used for parsing command-line arguments.

**pathlib**: Used for checking the existence of files at provided path.

**redlines**: Used for comparing original and edited translation segments.

**xml.etree.ElementTree**: Used for XLIFF files.

**sys**: Used for handling command-line arguments and errors.

## Installing and Running the Program

**1.** Clone the repository.

```
https://github.com/goncu/change_tracker.git
cd change-tracker
```

**2.** Create a virtual environment.

```
python3 -m venv venv
```

**3.** Activate the virtual environment.

- On macOS/Linux:

```
source venv/bin/activate
```

- On Windows:

```
venv\Scripts\activate
```

**4.** Install dependencies.

```
pip3 install -r requirements.txt
```

**5.** Run the program. The program accepts two mandatory arguments:

`- o` for the path to the original translation file.

`- e` for the path to the edited translation file.

Example:


```
python project.py -o original.xliff -e edited.xliff
```

This command will compare original.xliff with the edited.xliff and generate a report called changes.html in program's root folder.

## Testing

The program comes with several tests, written using the `pytest` framework. These tests ensure the correctness of various functions:

- **Test input validation**: Checks that invalid files or file paths result in an appropriate exit message.
- **Test text extraction**: Verifies that the extract_text function correctly extracts source and target text from a sample XLIFF file.
- **Test report generation**: Ensures that mismatched source texts trigger an exit, and an HTML file is generated when sources match.

To run the tests, use the following command:
```
pytest test_project.py
```

## Future Improvements
- Support for different files.
- GUI.

## Acknowledgements


This project was developed as [CS50P](https://cs50.harvard.edu/python/2022/) final project. Special thanks to the **CS50P team** for their exceptional course and support!





