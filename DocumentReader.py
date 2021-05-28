from abc import ABC, abstractmethod
from docx.api import Document


class DocumentReader(ABC):

    @abstractmethod
    def read_doc(self):
        pass


class PdfReader(DocumentReader):

    def read_doc(self):
        pass


class DocxReader(DocumentReader):
    """
    Returns a list of dictionaries for each row [{column:cell, column:cell},
                                                 {column:cell, column:cell}]
    """
    @classmethod
    def read_doc(cls, file):
        """returns data as rows"""
        document = Document(file)
        tables = document.tables

        table_list = []

        for table in tables:
            table_list.append(table)

        # list of dictionaries for each row eg. [column : value]
        data = []

        for table in table_list:
            for i, row in enumerate(table.rows):
                text = (cell.text for cell in row.cells)
                if i == 0:
                    keys = tuple(text)
                    continue
                row_data = dict(zip(keys, text))
                data.append(row_data)
        return data
