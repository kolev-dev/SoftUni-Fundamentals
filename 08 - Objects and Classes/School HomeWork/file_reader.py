class FileHandler:
    def read(self):
        pass

class TextFile(FileHandler):
    def read(self):
        return "Типа файл е TXT"

class CSVFile(FileHandler):
    def read(self):
        return "Типа файл е CSV"


txt_instance = TextFile()
csv_instance = CSVFile()

for file in [txt_instance, csv_instance]:
    print(file.read())