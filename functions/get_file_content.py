import os


def get_file_content(working_directory:str, file_path:str) -> str:
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path, file_path))
    valid_path= os.path.commonpath([target_dir, abs_path]) == abs_path

    if not valid_path:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    max_characteres= 10000
    try:

        with open(target_dir, "r", encoding="utf-8") as f:
            content= f.read(max_characteres)
            if f.read(1) != "":
                content += f'file "{file_path}" truncated to {max_characteres} characters'
            return content
        
    except Exception as e:
        
        return f"Error: {e}"
    

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "read the content of a specific file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description":  "where the file passed to the function is located",
                },
            },
            "required": ["file_path"]
        },
    },
    }

    