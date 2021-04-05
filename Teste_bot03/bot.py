# versão 6.0

import sqlite3

from sqlite3 import Error

class DataBase:
    __connection = None

    def get__connection(self, DataBase):
        if DataBase.__connection is None:
            DataBase.__connection = sqlite3.connect('BD_Leitura.db', check_same_thread=False)
        return DataBase.__connection
    
    vcon = get__connection 

    # Realizar consulta no banco
    def subscriber_exist(self, DataBase):
        conn = self.get__connection()
        c = conn.cursor()
        c.execute(f'SELECT * FROM BD_Leitura WHERE contrato = {2089890015}') #, (user_id,)) #SELECT * FROM BD_Leitura WHERE contrato =
        return (c.fetchall())
    
print(DataBase)    