This is regarding DAA mini project for SEM 4<br><br><br>

Team Member Details --<br>
<br>

1. Parth Sundarka<br>
2. Mahek Kamani<br>

Language Used --<br><br>

1. py<br><br>

Concept Demonstrated --<br>
Greedy Algorithm<br><br>

Problem Statement --<br><br>

To design a algorithm to get the maximum books for a library under a fixed amount.<br>
We have the book titles, available quantity, Price of each book and requirement of the library.<br>
The various Conditions implemented are --<br>
<br>

1. Books are not to be divided. It has to be sold as a whole<br>
2. Maximum Books are to be bought.<br>
3. If the availability is less than requested amount of books then the remaining books have to be updated in a file named NOT Fullfilled.csv with columns as<br>
   NAME OF THE BOOK | QUANTITY<br>
4. There are different sellers for each title of book, So we have to select the lowest cost of the title.<br>
5. The invoice for books bought has to be generated for books brought like the below format<br>

""SELLER NAME""<br>
NAME OF THE BOOK | QUANTITY | AMOUNT<br>
ENTRY | ENTRY | ENTRY<br>
.<br>
..<br>
...<br>
TOTAL -- Amount<br> 6. If a there is a request for 4 books and there are 2 sellers with availability of 1 and 2 books respectively then it should be bought from both the stores to fulfill the request. (Example) and remaining one should be updated in unfullfiled.csv<br> 7. After money is exhausted with the library all the books should be listed in the above file too in the requested format.<br>
