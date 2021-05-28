import pandas as pd
from DocumentReader import DocxReader
from configspec import configspec

data = DocxReader.read_doc('test.docx')

spec_list = configspec.read_spec("specfile.txt")

spec_row_dict = {}

# filter rows to tables we specified
for i, spec in enumerate(spec_list):
    spec_row_dict[str(i)] = [row for row in data if row.keys() == set(spec)]

# save each appended table spec to a csv
for i, (key, value) in enumerate(spec_row_dict.items()):
    df = pd.DataFrame(value)
    df.to_csv("Sample {}.csv".format(i))
