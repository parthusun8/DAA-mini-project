## Create Invoice here #########


################################
import os
import pandas as pd


def invoice(bought_books):
    sellers_list = {}
    for book in bought_books:
        for seller in bought_books[book]:
            if seller[0] not in sellers_list:
                sellers_list[seller[0]] = [[book, seller[1], seller[2]]]
            else:
                sellers_list[seller[0]].append([book, seller[1], seller[2]])
    return sellers_list


def create_invoice(sellers_list):
    for seller in sellers_list:
        # print(seller)
        title = []
        quantity = []
        amount = []
        total = []
        sum = 0
        for book in sellers_list[seller]:
            title.append(book[0])
            quantity.append(book[1])
            amount.append(book[2])
            total.append(book[1] * book[2])
            sum += book[1] * book[2]
        title.append("Total")
        quantity.append("")
        amount.append("")
        total.append(sum)
        data = {"Title": title, "Quantity": quantity, "Amount": amount, "Total": total}
        print(data)
        df = pd.DataFrame(data)
        df.to_csv(f"./invoice/{seller}.csv", index=False)


if __name__ == "__main__":
    print("Used in main.py only")
