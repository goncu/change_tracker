from pathlib import Path

import argparse
import sys


def check_input(arguments):
    # create parser object for parsing command line arguments
    parser = argparse.ArgumentParser(
        prog="project.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="CHANGE TRACKER\n\nThis command line utility takes two files,\none with original translation and the other with edited translation,\nand generates a report with changes tracked in the same folder with the program.",
    )

    # add arguments
    parser.add_argument("-o", help="Path to file with original translation")
    parser.add_argument("-e", help="Path to file with edited translation")

    # check for arguments' existence
    if len(sys.argv) == 1:
        sys.exit(parser.print_help())

    # parse arguments
    args = parser.parse_args(arguments)

    # check for arguments validity
    if not Path(args.o).exists() or not Path(args.e).exists():
        sys.exit("One or more files not found. Please check file paths and try again.")

    # check file extension
    if not args.o.endswith(".xliff") or not args.e.endswith(".xliff"):
        sys.exit(
            "One or more files are not in XLIFF format. Please check and try again."
        )

    return args.o, args.e


def extract_text(file):
    return 1, 2


def generate_report(
    source_from_original, source_from_edited, translation_original, translation_edited
): ...
