# -*- coding: utf-8 -*-
"""
Created on Sun May 23 15:45:44 2021

@author: lapechie
"""
import pandas as pd
from docx.api import Document

#####################################################################
# Part 1 - Read table data from doc #################################
#####################################################################

# read the doc
# future enhancement: make it read all doc files in directory
document = Document('test.docx')

# tables in the document
tables = document.tables

# create a list of tables
table_list = []

for table in tables:
    table_list.append(table)


# loop through tables and create a list of dictionaries for each row eg. [column : value]
data = []

for table in table_list:
    for i, row in enumerate(table.rows):
        text = (cell.text for cell in row.cells)

        if i == 0:
            keys = tuple(text)
            continue
        row_data = dict(zip(keys, text))
        data.append(row_data)
 
    
for row in data:
   print(row)
   
#####################################################################
# Part 2 - Read specfile ############################################
#####################################################################       
     
specfile = open("specfile.txt", "r")

lines = specfile.read().splitlines()

spec_list = [ line.split(",") for line in lines]   
 
#####################################################################
# Part 3 - Store tables that match spec list ########################
#####################################################################

spec_row_list = []

for spec in spec_list:      
    for row in data:
        if row.keys()==set(spec):
            spec_row_list.append(row)
            
            

# print(spec_row_list)




#print(data[0].keys()==set(['Primary_Key', 'Feature_1', 'Feature_2', 'Feature_3']))

df = pd.DataFrame(spec_row_list)
print(df)



