import read_files

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


if __name__ == "__main__":
    main()
