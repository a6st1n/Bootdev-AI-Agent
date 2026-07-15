import os

def write_file(working_directory:str,file_path:str, content:str):
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path, file_path))
    valid_path= os.path.commonpath([target_dir, abs_path]) == abs_path
    os.makedirs(os.path.dirname(target_dir), exist_ok=True)

    
    if not valid_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(target_dir):
        return f'Error: cannot write to "{file_path}" as it is a directory'

    

    try:
        with open(target_dir, "w", encoding="utf-8") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    
            

