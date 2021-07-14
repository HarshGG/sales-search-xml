# Sales Search XML

Description: given a data file `sales-data.xml` that contains 1,000 random sales from between 8/1/2019 and 8/30/2020, the program parses data out of this file.<br>
Language: Python<br>
Program type: School project, solo<br>
Purpose: : Analyze how to use Python's useful features to parse and examine XML Datafiles <br>

### Amount Spent

The first method, `amount_spent`, goes through the data file and finds the amount spent in a specified category. For example, `amount_spent('Baby')` would return the amount spent in the `Baby` category.

### Spent by Gender

`spent_by_gender` returns a dictionary with the amount spent for each gender. Keys should be `"M"` and `"F"`.  Key order does not matter. 

Be sure to run your dictionary through `round_dictionary` before returning. 

### All Categories

`all_categories` returns a dictionary of the amount spent in each category, with the category name as key and amount as value. 

### Spent Between

The `spent_between` method takes a `start_date` and `end_date` and returns the amount of sales between those two dates, inclusive.
