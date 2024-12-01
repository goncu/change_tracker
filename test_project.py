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
    org1 = [{"source": "a", "target": "b"}]
    edt1 = [{"source": "c", "target": "d"}]
    with pytest.raises(SystemExit):
        generate_report(org1, edt1)

    org2 = [{"source": "a", "target": "b"}]
    edt2 = [{"source": "a", "target": "c"}]

    assert generate_report(org2, edt2)

