import pandas


requirements_file = "req.csv"


############# GET ALL SELLERS HERE #########

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
