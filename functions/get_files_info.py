import os


def get_files_info(working_directory: str, directory:str=".") -> str:
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path, directory))
    valid_path= os.path.commonpath([target_dir, abs_path]) == abs_path

    
    if not valid_path:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(target_dir):
        return f'Error: Directory "{directory}" is not a directory'
    
    
    listed_files=[]
    try:
        for files in os.listdir(target_dir):
            file_name = os.path.basename(files)
            file_size = os.path.getsize(os.path.join(target_dir, files))
            is_directory = os.path.isdir(os.path.join(target_dir, files))
            listed_files.append(f'- {file_name}: file_size={file_size} bytes, is_dir={is_directory}')
    except Exception as e:
        return f"Error: {e}"
    return "\n".join(listed_files)

    
    
        