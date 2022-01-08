import csv,json
from pathlib import Path
from typing import Text
from TextHelper import TextHelper

class FileTool:

    def __init__(self, path, fields = []):
        self.path = path
        self.fields = fields

    def isFileExist(self):
        """
            - Helper method that checks the file exist or not
            - The function returns bool 
        """
        return Path(self.path).exists()

    def create_new_file(self):
        """
            This method is used to create a new file 
        """
        file_name = input(TextHelper.ASK_FOR_FILE_NAME)
        file_format = input(TextHelper.ASK_FOR_FILE_FORMAT)

        try:
            open(file_name+"."+file_format,"x")
        except:
            print(TextHelper.SAME_FILE_EXCEPTION)

    def read_file_content(self):
        """
            This method is used to read 
            all data from files.
        """
        with open(self.path, "r") as file:
            contents = file.read()
            print(contents)
    
    def csv_operations(self):
        """
        List of operations:
            [1] CSV to TXT 
            [2] CSV to JSON
            [3] Print a line from CSV
        """
        choice = input(TextHelper.CSV_OPERATIONS_MENU)

        if choice == "1":
            if Path(self.path).suffix == ".csv":
                if self.isFileExist():
                    txt_file_name = input(TextHelper.ASK_FOR_TXT_FILE_NAME)
                    with open(txt_file_name+".txt", "w") as txt_file:
                        with open(self.path,"r") as csv_file:
                            for row in csv.reader(csv_file):
                                txt_file.write(" ".join(row)+"\n")  
                    print(TextHelper.SUCCESS_MESSAGE)
                else:
                    print(TextHelper.NO_FILE_EXCEPTION)
            else:
                print(TextHelper.UNMATCHED_FILE_TYPE_EXCEPTION)
        
        elif choice == "2":
            if Path(self.path).suffix == ".csv":
                if self.isFileExist():

                    data = [] # for the collecting each line of csv
                    with open(self.path) as csv_file:
                        csv_content = csv.DictReader(csv_file)
                        for rows in csv_content:
                            data.append(rows)

                    json_file_name = input(TextHelper.ASK_FOR_JSON_FILE_NAME)

                    with open(json_file_name+".json","w") as json_file:
                        json_content = json.dumps(data, indent = 4) 
                        json_file.write(json_content)
                    print(TextHelper.SUCCESS_MESSAGE)

                else:
                    print(TextHelper.NO_FILE_EXCEPTION)
            else:
                print(TextHelper.UNMATCHED_FILE_TYPE_EXCEPTION)

        elif choice == "3":
            import pandas as pd
            df = pd.read_csv(self.path)

            print(TextHelper.GLIMPSE_MESSAGE)
            print(df.head(10))

            line = int(input(TextHelper.ASK_FOR_WHICH_LINE))
            print(df.iloc[line])

        else:
            print(TextHelper.INVALID_OPERATION_TYPE_EXCEPTION)

    def json_operations(self):
        """
            This method is used to 
            [1] imports whole contents of json into txt file.
            [2] imports whole contents of txt into json file.
        """
        choice = input(TextHelper.JSON_OPERATIONS_MENU)

        if choice == "1":
            if Path(self.path).suffix == ".json": # checks whether file is a json file or not
                if self.isFileExist(): # checks whether file exits
                    with open(self.path,"r") as json_file: # opens json file
                        json_content = json.load(json_file) # takes whole contents of json file

                    new_file_name = input(TextHelper.ASK_FOR_TXT_FILE_NAME) # asks for nw txt file name
                    with open(new_file_name+".txt","w+") as new_file:
                        new_file.write(str(json_content)) # writes the whole content of json file to nw txt file

                    print(TextHelper.SUCCESS_MESSAGE)
                else:
                    print(TextHelper.NO_FILE_EXCEPTION)
            else:
                print(TextHelper.UNMATCHED_FILE_TYPE_EXCEPTION)

        elif choice == "2":
            if Path(self.path).suffix == ".txt":
                if self.isFileExist():
                    file_content = {}
                    with open(self.path) as file:
                        for line in file:
                            command, description = line.strip().split(None, 1)
                            file_content[command] = description.strip()
                        
                    new_file_name = input(TextHelper.ASK_FOR_JSON_FILE_NAME)

                    with open(new_file_name+".json","w") as file:
                        json.dump(file_content,file,indent = 4, sort_keys = False)
                    print(TextHelper.SUCCESS_MESSAGE)
                else:
                    print(TextHelper.NO_FILE_EXCEPTION)
            else:
                print(TextHelper.UNMATCHED_FILE_TYPE_EXCEPTION)
        else:
                print(TextHelper.INVALID_OPERATION_TYPE_EXCEPTION)

    def file_operations(self):
        """
            This method is used to File Operations like 
                [1] searching, 
                [2] reading,
                [3] updating,
                [4] deleting.
                [5] print the whole content of file
        """
        if self.isFileExist():
            choice = input(TextHelper.FILE_OPERATIONS_MENU) # takes input from the user

            if choice == "1": # searching operation, if choice 1
                key = input(TextHelper.ASK_FOR_SEARCH) # the user enters the word to be searched
                with open(self.path) as file:
                    contents = file.readlines() # reads all lines
                found_lines = [ data for data in contents if key in data ] # creates a list that if matches that desired word with content

                if len(found_lines) != 0: # if there are some matcing, prints
                    print(f"{key} found in {len(found_lines)} lines: \n", *found_lines)
                else: # if no match
                    print(TextHelper.NO_MATCH_FOR_SEARCH)
            
            elif choice == "2": # deleting operation, if choice 2
                key = input(TextHelper.ASK_FOR_DELETE) # the user enters the word to be deleted
                current_file = open(self.path)
                updated_file = open("updated_"+self.path,"w")
                
                for line in current_file:
                    if key in line:
                        updated_file.write(line.replace(key,""))
                    else:
                        print(TextHelper.NO_MATCH_FOR_SEARCH)
                        break
                current_file.close()
                updated_file.close()
                
            elif choice == "3": # adding operation, if choice 3
                key = input(TextHelper.ASK_FOR_ADD)
                with open(self.path, "a+") as file:
                    file.write("\n"+key)
                print(TextHelper.SUCCESS_MESSAGE)

            elif choice == "5":
                self.read_file_content() # reads the whole content of file
            else:
                print(TextHelper.INVALID_OPERATION_TYPE_EXCEPTION)
        else:
            print(TextHelper.NO_FILE_EXCEPTION)

if __name__ == "__main__":

    file_path = 'heart.csv'
    ft = FileTool(file_path)
    ft.csv_operations()