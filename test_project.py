from helpers import check_input, extract_text, generate_report
import pytest


def test_check_input():
    with pytest.raises(SystemExit):
        check_input(["-o", "a.xliff", "-e", "b.xliff"])

    with pytest.raises(SystemExit):
        check_input(["-o", "test/or.txt", "-e", "test/ed.txt"])


def test_extract_text(): 
    assert extract_text('test/test.xliff') == [{'source': 'a', 'target': 'b'}]


def test_generate_report():
    org = [{"source": "a", "target": "b"}]
    edt = [{"source": "c", "target": "d"}]
    with pytest.raises(SystemExit):
        generate_report(org, edt)
