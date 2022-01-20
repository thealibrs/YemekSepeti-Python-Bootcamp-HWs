from constants.messages import CustomMessages
from model.user import User
from helpers.file_helper import FileHelper
from helpers.database_helper import DatabaseHelper

def main(file = None, db = None):
    
    if (file is not None) and (db is not None):
        jsonFileTool = FileHelper()
        databaseHelper = DatabaseHelper(db)

        userInfoList = jsonFileTool.scrapJsonFile(file)
        databaseHelper.createTable()

        for user_info in userInfoList:
            databaseHelper.insertData(user_info)
    else:
        print(CustomMessages.PARAMETER_ERROR)


if __name__ == "__main__":

    file = "dataregex.json"
    db = "dataregex.db"

    main(file,db)
