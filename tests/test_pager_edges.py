from src.pager import fidelity_page_window


def test_empty_rows():
    assert fidelity_page_window([], 1, 2) == []
