class TextHelper:
    """
    This class was created for enrich 
    the readability of FileTool class.
    """
    # exceptions message
    NO_FILE_EXCEPTION = "There is no file in the given path!"
    UNMATCHED_FILE_TYPE_EXCEPTION = "Unmatched file type!"
    INVALID_OPERATION_TYPE_EXCEPTION = "Invalid operation type!"
    SAME_FILE_EXCEPTION = "There is same file in given path"

    # menu messages
    JSON_OPERATIONS_MENU = "\nList of operations:\n\n[1] JSON to TXT\n[2] TXT to JSON\n"
    FILE_OPERATIONS_MENU = "\nList of operations:\n\n[1] Searching\n[2] Deleting\n[3] Adding\n[4] Updating\n[5] Show Content\n"
    CSV_OPERATIONS_MENU = "\nList of operations:\n\n[1] CSV to TXT \n[2] CSV to JSON\n[3] Print a line from CSV\n"

    # input messages
    ASK_FOR_FILE_NAME = "Enter file name: "
    ASK_FOR_TXT_FILE_NAME = "Enter file name for txt file: "
    ASK_FOR_JSON_FILE_NAME = "Enter file name for json file: "
    ASK_FOR_DELETE = "Enter a word that you want to delete from the file: "
    ASK_FOR_SEARCH = "Enter a word that you want to search: "
    ASK_FOR_ADD = "Enter anything that you want to add: "
    ASK_FOR_FILE_FORMAT = "Write file format?\n- csv\n- json\n- txt\n"
    ASK_FOR_WHICH_LINE = "Enter a line number for printing: \n"

    # output messages
    SUCCESS_MESSAGE = "Operation Succes!"
    NO_MATCH_FOR_SEARCH = "Nothing matched in the content!"
    GLIMPSE_MESSAGE = "Here is your data content...\n"
