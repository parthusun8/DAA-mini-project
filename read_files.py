import pandas as pd
import os


def requirement():
    requirements_file = "./Helper/req.csv"
    dataframe = pd.read_csv(requirements_file)
    requirements = {}
    for data in dataframe.iterrows():
        requirements[data[1][0]] = data[1][1]

    return requirements
    ############# GET ALL SELLERS HERE #########


def sellers(requirements):
    sellers_list = os.listdir("./Sellers")

    no_of_sellers = len(sellers_list)
    available_books = {}
    for seller in sellers_list:
        data = pd.read_csv("./Sellers/" + seller)
        for d in data.iterrows():
            title = d[1][0]
            quantity = d[1][1]
            amount = d[1][2]
            seller_name = seller.split(".")[0]
            if title in requirements:
                if title not in available_books:
                    available_books[title] = [[seller_name, quantity, amount]]
                else:
                    available_books[title].append([seller_name, quantity, amount])

    for book in available_books:
        available_books[book] = sorted(available_books[book], key=lambda x: x[2])

    return available_books, no_of_sellers


if __name__ == "__main__":
    print("This should be used as a module in main.py")


############################################


############ Get Books per seller which are requested ##############
#### Try Store everything as dictionaries ##########################


####################################################################


######## Create a list for every book which has a nested list with entries of the format of dictionary like -- #######
##### {seller_name : amount per book} for each seller


###################################################################################################


####### Apply Dynamic or greedy to find best seller and amount for each book########
### There might be more than one seller selected for each book as if one seller has less quantity of books ######
#### Then it is selected from the next inexpensive seller ############################


###############################################################################################################


########## From above get the fulfillment of each book in the format {seller: quantity} ##########
# We need not store the amount as it can be found using book title and seller name from step 1 ########


#####################################################################################################


#### Return the above dictionary to main program ##########################################


###########################################################################################


### Add unfulfilled request in unfulfilled.csv ############################################


###########################################################################################
