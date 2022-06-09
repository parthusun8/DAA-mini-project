This is regarding DAA mini project for SEM 4

Team Member Details --

1. Parth Sundarka
2. Mahek Kamani

Language Used --

1. py

Concept Demonstrated --
Greedy Algorithm

Problem Statement --

To design a algorithm to get the maximum books for a library under a fixed amount.
We have the book titles, available quantity, Price of each book and requirement of the library.
The various Conditions implemented are --

1. Books are not to be divided. It has to be sold as a whole
2. Maximum Books are to be bought.
3. If the availability is less than requested amount of books then the remaining books have to be updated in a file named NOT Fullfilled.csv with columns as
   NAME OF THE BOOK | QUANTITY
4. There are different sellers for each title of book, So we have to select the lowest cost of the title.
5. The invoice for books bought has to be generated for books brought like the below format

""SELLER NAME""
NAME OF THE BOOK | QUANTITY | AMOUNT
ENTRY | ENTRY | ENTRY
.
..
...
TOTAL -- Amount 6. If a there is a request for 4 books and there are 2 sellers with availability of 1 and 2 books respectively then it should be bought from both the stores to fulfill the request. (Example) and remaining one should be updated in unfullfiled.csv 7. After money is exhausted with the library all the books should be listed in the above file too in the requested format.
