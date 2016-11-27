---------------------------------------
 THE INSTANCE FORMAT IS THE FOLLOWING:
---------------------------------------

NbItems KnapsackSize
<< And then for each item >>
Index Profit Weight [List_Of_Conflict_Items]

----------------------------------------
SOLUTION FORMAT SHOULD BE THE FOLLOWING:
----------------------------------------

NbItemsUsed TotalWeight TotalProfit
<< And then for each item placed in the knapsack >>
ItemIndex FractionOfItem

----------------------------------------
              SOME REMARKS:
----------------------------------------

* The second field, "FractionOfItem" belongs between [0,1]. For the questions 2 and 3, they should always be
set to 1 (item cannot be fractioned).

* The instances are common for all three questions.
They include all the information : weight, profit for the items as well as their conflicts  (for question 3).
When you read the instances and are not solving the question 3, simply ignore the information about the conflicts.

* Your code should be called using the following commandline "executable instancePath Q", where Q can take value 1,2,3 depending on which question you are solving.

* Example of a solution file with 4 items {2,5,8,12} all items of weight 3 and profit 5

4 12 20
2 1
5 1
8 1
12 1
