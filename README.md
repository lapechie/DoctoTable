# Document-to-Table
## Purpose
Scrapes specified table columns from documents and appends for each re-occuring specified structure.

## Requirements
pip install python-docx

## Example

Suppose below tables are present in a document.

We can specify what tables we cant to scrape in the spec.

### Spec Example:

Product,Category,Price,Availability

Financials,Revenue,Storage Costs,Waste
 
### Store A

| Product	    |Category	   |Price |	Availability  |
|---------------|--------------|------|---------------|
| Shovel	    |Digging Tools |15	  |54             |
| Pickaxe	    |Digging Tools |22	  |79             |
| Hedge Trimmer	|Garden Tools  |179	  |6              |
| Lawn Mower	|Garden Tools  |399	  |8              |

| Financials	|Revenue	   |Storage Costs |	Waste  |
|---------------|--------------|--------------|--------|
| Shovel	    |1000          |5	          |1       |
| Pickaxe	    |2000          |10	          |0       |
| Hedge Trimmer	|5000          |25            |0       |
| Lawn Mower	|1200          |50	          |0       |


### Store B

| Product	    |Category	   |Price |	Availability  |
|---------------|--------------| -----|---------------|
| Apple	        |Fruit         |1	  |300            |
| Peach	        |Fruit         |2	  |400            |
| Pineapple	    |Fruit         |4	  |100            |
| Kiwi   	    |Fruit         |1	  |200            |

| Financials	|Revenue	   |Storage Costs |	Waste  |
|---------------|--------------|--------------|--------|
| Apple	        |5000         |10	          |20      |
| Peach	        |5675         |20	          |10      |
| Pineapple	    |3456         |10	          |2       |
| Kiwi   	    |3456         |10	          |8       |


### Store C

| Product	    |Category	   |Price |	Availability  |
|---------------|--------------| -----|---------------|
| Lamb	        |Meat          |22	  |25             |
| Chicken	    |Meat          |12	  |25             |
| Beef	        |Meat          |26	  |30             |
| Turkey	    |Meat          |16	  |5              |

| Financials	|Revenue	   |Storage Costs |	Waste  |
|---------------|--------------|--------------|--------|
| Lamb	        |4000          |30	          |20      |
| Chicken	    |5000          |40	          |30      |
| Beef	        |6000          |20	          |40      |
| Turkey	    |7000          |20	          |80      |

### Output

The document is scraped for the tables.

Outputs are tables specified as csvs.

Table 1:

| Product	    |Category	   |Price |	Availability  |
|---------------|--------------|------|---------------|
| Shovel	    |Digging Tools |15	  |54             |
| Pickaxe	    |Digging Tools |22	  |79             |
| Hedge Trimmer	|Garden Tools  |179	  |6              |
| Lawn Mower	|Garden Tools  |399	  |8              |
| Apple	        |Fruit         |1	  |300            |
| Peach	        |Fruit         |2	  |400            |
| Pineapple	    |Fruit         |4	  |100            |
| Kiwi   	    |Fruit         |1	  |200            |
| Lamb	        |Meat          |22	  |25             |
| Chicken	    |Meat          |12	  |25             |
| Beef	        |Meat          |26	  |30             |
| Turkey	    |Meat          |16	  |5              |


Table 2:

| Financials	|Revenue	   |Storage Costs |	Waste  |
|---------------|--------------|--------------|--------|
| Shovel	    |1000          |5	          |1       |
| Pickaxe	    |2000          |10	          |0       |
| Hedge Trimmer	|5000          |25            |0       |
| Lawn Mower	|1200          |50	          |0       |
| Apple	        |5000         |10	          |20      |
| Peach	        |5675         |20	          |10      |
| Pineapple	    |3456         |10	          |2       |
| Kiwi   	    |3456         |10	          |8       |
| Lamb	        |4000          |30	          |20      |
| Chicken	    |5000          |40	          |30      |
| Beef	        |6000          |20	          |40      |
| Turkey	    |7000          |20	          |80      |

### Future Enhancements
Make the first column of each row in the spec file be the name of the table e.g. Table Name, column1, column2, ...
