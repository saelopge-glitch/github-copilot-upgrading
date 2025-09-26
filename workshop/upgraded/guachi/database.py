# Python 3.12 호환 버전 (legacy에서 변환됨)
import sqlite3

class dbdict(dict):
    def __init__(self, path, table='_guachi_data'):
        dict.__init__(self)
        self.table = table
        self.db_filename = path
        self.con = sqlite3.connect(self.db_filename)
        # ... 나머지 코드는 legacy/database.py에서 Python 3.12에 맞게 수정된 버전 ...
