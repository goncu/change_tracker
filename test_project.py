from helpers import check_input, extract_text, generate_report
import pytest


def test_check_input():
    with pytest.raises(SystemExit) as error:
        check_input(["-o", "thisfile.xliff", "-e", "doesnotexist.xliff"])
    assert error.type == SystemExit
    assert (
        error.value.code
        == "One or more files not found. Please check file paths and try again."
    )

    with pytest.raises(SystemExit) as error2:
        check_input(["-o", "samples/or.txt", "-e", "samples/ed.txt"])
    assert error2.type == SystemExit
    assert (
        error2.value.code
        == "One or more files are not in XLIFF format. Please check and try again."
    )


def test_extract_text(): ...


def test_generate_report(): ...
