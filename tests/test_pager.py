from src.pager import fidelity_page_window


def test_last_page_has_no_extra_row():
    assert fidelity_page_window([1, 2, 3], 2, 2) == [3]
