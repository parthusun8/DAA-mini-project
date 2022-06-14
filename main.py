import read_files
from invoice.invoice import invoice, create_invoice
import selection


def main():

    ## GET LIBRARY REQUIREMENTS FOR BOOKS
    requirements = read_files.requirement()
    available_books, no_of_sellers = read_files.sellers(requirements)
    print(available_books)

    unfulfilled, all_selections = selection.select(requirements, available_books)

    read_files.update_unfulfilled_csv(unfulfilled)

    sellers = invoice(available_books)

    create_invoice(sellers)


if __name__ == "__main__":
    main()
