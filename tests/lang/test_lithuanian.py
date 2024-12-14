import pytest

LT_RULES_TEST_CASES = [
    ("– Labas! – švelniai tarė.", ["– Labas! – švelniai tarė."]),
    ("– Kaip laikaisi? – žvaliai paklausė.", ["– Kaip laikaisi? – žvaliai paklausė."]),
]


@pytest.mark.parametrize("text,expected_sents", LT_RULES_TEST_CASES)
def test_lt_sbd(lt_default_fixture, text, expected_sents):
    """Lithuanian language SBD tests"""
    segments = lt_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
