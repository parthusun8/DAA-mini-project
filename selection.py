def select(req, books):
    all_selections = {}
    for book in req:
        selection = []
        current_sellers_for_book = books[book]
        for b in current_sellers_for_book:
            if req[book] <= b[1]:
                b[1] = req[book]
                selection.append(b)
                req[book] = 0
                break
            else:
                selection.append(b)
                req[book] -= b[1]
        # print(book, selection)
        all_selections[book] = selection
    unfulfilled = {}
    for book in req:
        if req[book] != 0:
            unfulfilled[book] = req[book]
    return unfulfilled, all_selections


if __name__ == "__main__":
    print("Used in main.py as a module")
