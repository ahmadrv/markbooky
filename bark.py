import sqlite3

class DatabaseManager:
    def __init__(self, database_filename) -> None:
        self.conncetion = sqlite3.connect(database_filename)
    
    def __del__(self) -> None:
        self.conncetion.close()
    
    def _execute(self, statement):
        with self.conncetion:
            cursor = self.conncetion.cursor()
            cursor.execute(statement)
            return cursor

    def create_table(self, table_name, columns):
        columns_with_types = [
            f'{column_name} {data_type}'
            for column_name, data_type in columns.items()
        ]
        
        self._execute(
            f'''
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            '''
        )
    
    def add(self, table_name, data):
        placeholders = ', '.join('?' * len(data))
        column_names = ', '.join(data.keys())
        column_values = tuple(data.values())
        
        self._execute(
            f'''
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            ''',
            column_values,
        )
        
if __name__ == '__main__':
    test = DatabaseManager('test.db')
    
    print(test)
    
    del test