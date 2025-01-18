import pytest

LT_RULES_TEST_CASES = [
    ("– Labas! – švelniai tarė.", ["– Labas! – švelniai tarė."]),
    ("– Kaip laikaisi? – žvaliai paklausė.", ["– Kaip laikaisi? – žvaliai paklausė."]),
    ("– Kaip laikaisi? – žvaliai paklausė.", ["– Kaip laikaisi? – žvaliai paklausė."]),
    (
        "– Kaip tu drįsti, Petrai?! – pasakė Jonas. – Lengvai.",
        ["– Kaip tu drįsti, Petrai?! – pasakė Jonas.", "– Lengvai."],
    ),
    ("– Sa, Brisiau, sa!..", ["– Sa, Brisiau, sa!.."]),
    (
        "– A tu, žabali, ar nenustosi!.. Savo žmogaus nemato, – girdi jisai pažįstamą balsą.",
        [
            "– A tu, žabali, ar nenustosi!..",
            "Savo žmogaus nemato, – girdi jisai pažįstamą balsą.",
        ],
    ),
    (
        "Juk jisai nekaltas… Brisius nori pasigerinti, suvizginti uodegą, bet iš baimės tupiasi ant paskutinių kojų, ir per jo snukį rieda gailios karčios ašaros.",
        [
            "Juk jisai nekaltas…",
            "Brisius nori pasigerinti, suvizginti uodegą, bet iš baimės tupiasi ant paskutinių kojų, ir per jo snukį rieda gailios karčios ašaros.",
        ],
    ),
]


@pytest.mark.parametrize("text,expected_sents", LT_RULES_TEST_CASES)
def test_lt_sbd(lt_default_fixture, text, expected_sents):
    """Lithuanian language SBD tests"""
    segments = lt_default_fixture.segment(text)
    segments = [s.strip() for s in segments]
    assert segments == expected_sents
