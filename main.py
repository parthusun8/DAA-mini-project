import read_files
from invoice.invoice import invoice, create_invoice

#  from project.folder.subfolder.filename import functionname


## There can n sellers and not necessary that each seller will have all books


def main():

    ## GET LIBRARY REQUIREMENTS FOR BOOKS
    requirements = read_files.requirement()
    print("\nLibrary requirements are -- ")
    for book in requirements:
        print(f"\tNeeded {requirements[book]} pieces for {book}")

    ## GET ALL BOOKS AND PRICE OFFERED BY VARIOUS SELLERS
    available_books, no_of_sellers = read_files.sellers(requirements)
    print("\n BOOKWISE SELLERS ARE (in sorted order is ) -- ")
    for book in available_books:
        print(book)
        for seller in available_books[book]:
            print("\t", seller)

    ## Generating seller wise data (To be changed when algorithm for selecting books is done)
    sellers = invoice(available_books)

    # Creating invoice for each seller
    create_invoice(sellers)


if __name__ == "__main__":
    main()
