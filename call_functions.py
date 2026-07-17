from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content


#available functions to use in the chatbot
available_functions_to_use = [schema_get_files_info,schema_get_file_content]