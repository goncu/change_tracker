from pathlib import Path
from redlines import Redlines
import xml.etree.ElementTree as ET
import argparse
import sys


def check_input(arguments):
    # create parser object for parsing command line arguments
    parser = argparse.ArgumentParser(
        prog="project.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description="CHANGE TRACKER\n\nThis command line utility takes two files,\none with original translation and the other\nwith edited translation, and generates a report\nwith the name 'changes.html', showing both source\nand changes, if any, segment by segment,\nin a table format. The report is generated\nin the same folder with the program.",
    )

    # add arguments
    parser.add_argument("-o", help="Path to file with original translation")
    parser.add_argument("-e", help="Path to file with edited translation")

    # check for arguments' existence
    if len(sys.argv) == 1:
        sys.exit(parser.print_help())

    # parse arguments
    args = parser.parse_args()

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
    # parse xml
    tree = ET.parse(file)
    root = tree.getroot()
    trans_units = root.findall(".//trans-unit")
    # list to hold source and translation text
    text = []
    # extract source and translation text from translation units and append them to the list.
    for unit in trans_units:
        source = unit.find("source")
        target = unit.find("target")

        text.append(
            {
                "source": source.text if source is not None else "",
                "target": target.text if target is not None else "",
            }
        )
    return text


def generate_report(original, edited):
    # check if sources are identical
    for org, edt in zip(original, edited):
        if org["source"] != edt["source"]:
            sys.exit(
                "Sources do not match. Please make sure you are comparing correct files."
            )
    # check for differences and create html file
    with open("changes.html", "w", encoding="utf-8") as file:
        file.write(
            f'<table border="1" align="center"><thead><tr><th>Source</th><th>Translation</th></tr></thead><tbody>'
        )
        for org, edt in zip(original, edited):
            changes = Redlines(org["target"], edt["target"])
            file.write(
                f'<tr><td>{org["source"]}</td><td>{changes.output_markdown}</td>'
            )
        file.write("</tbody></table>")
    return True
