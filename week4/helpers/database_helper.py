import sqlite3
from constants.messages import CustomMessages
from model.user import User
from datetime import date

class DatabaseHelper:
    def __init__(self, db_name):
        self.db_name = db_name

    def getTableName(self):
        """Returns the table name"""
        current_date = str(date.today().year)+str(date.today().month)+str(date.today().day)
        table_name = "data_"+current_date

        return table_name

    def createConnection(self):
        connection = None
        try:
            connection = sqlite3.connect(self.db_name)
            return connection
        except:
            print(CustomMessages.DB_CONNECTION_ERROR)

    def createTable(self):
        try:
            connection = self.createConnection()
            cursor = connection.cursor()
            
            create_table_script = f'''CREATE TABLE IF NOT EXISTS {self.getTableName()}
              (username TEXT, name_surname TEXT, 
              email TEXT, emailuserlk TEXT,
              usernamelk TEXT, birth_year TEXT,
              birth_month TEXT, birth_day TEXT,
              country TEXT, active_passive TEXT
              )'''

            cursor.execute(create_table_script)
            connection.commit()

            print(CustomMessages.DATABASE_CREATE_SUCCES)
            
        except:
            print(CustomMessages.DB_CREATE_SUCCES)
        finally:
            connection.close()

    def insertData(self, user:User):
        try:
            connection = self.createConnection()
            insert_script =  f''' INSERT INTO {self.getTableName()}
            (username, name_surname, email, 
            emailuserlk, usernamelk, birth_year,
            birth_month,birth_day,country,active_passive
            ) 
            VALUES(
                "{user.username}","{user.name_surname}",
                "{user.email}","{user.emailuserlk}",
                "{user.usernamelk}","{user.birth_year}",
                "{user.birth_day}","{user.birth_month}",
                "{user.country}", "{user.active_passive}"
                ) '''
            
            cursor = connection.cursor()
            cursor.execute(insert_script)
            connection.commit()
            print(CustomMessages.DATA_INSERT_SUCCES)

        except:
            print(CustomMessages.DATA_INSERT_ERROR)
            
        finally:
            connection.close()



           







       
