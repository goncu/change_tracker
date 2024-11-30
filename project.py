from helpers import check_input, extract_text, generate_report
import sys


def main():
    # check for command line arguments' validity
    original_file, edited_file = check_input(sys.argv)

    # extract source and target texts from file with original translation
    source_and_original_translation = extract_text(original_file)

    # extract source and target texts from file with edited translation
    source_and_edited_translation = extract_text(edited_file)

    # generate changes report
    generate_report(source_and_original_translation, source_and_edited_translation)


if __name__ == "__main__":
    main()
