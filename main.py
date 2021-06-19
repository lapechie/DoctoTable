import csv
from DocumentReader import DocxReader
from configspec import read_spec

spec_list = read_spec("specfile.txt")

test_doc = DocxReader('test.docx', spec_list)

# save each appended table spec to a csv
for key, value in test_doc.tables.items():
    with open(f"Sample {key}.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=value[0].keys())
        writer.writeheader()
        writer.writerows(value)
