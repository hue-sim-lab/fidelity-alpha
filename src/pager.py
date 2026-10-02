PAGE_LIMIT = 50


def fidelity_page_window(rows, page, size):
    # fidelitymarker
    start = (page - 1) * size
    return rows[start:start + size + 1]
