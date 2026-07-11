def get_files_info(working_directory: str, directory:str=".") -> str:
    target_dir = os.path.normpath(os.path.join(working_directory, directory))