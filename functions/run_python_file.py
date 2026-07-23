import os
import subprocess

def run_python_file(
        working_directory:str, file_path:str, args: list[str] | None = None
) -> str:
    abs_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_path, file_path ))
    valid_path= os.path.commonpath([target_dir, abs_path]) == abs_path

    
    if not valid_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(target_dir):
        return f'Error: "{file_path}" does not exist or is not a file'
    
    if not target_dir.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    commands = ["python", target_dir]
    if args:
        commands.extend(args)
    
    try:
        run = subprocess.run(commands,cwd=working_directory, capture_output=True, text=True, timeout=30)
        if run.returncode != 0:
            return f"process exited with code {run.returncode}"
        if run.stdout == "" and run.stderr == "":
            return "No output produced"
        else:
            return f"STDOUT: {run.stdout}\nSTDERR: {run.stderr}"
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "runs any python file inside the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "where the file passed to the function is located",
                },
                "args":{
                    "type": "array",
                    "items":{
                        "type": "string"
                    },
                    "description": "optional CL arguments passed to the python file before running"
                }
            },
            "required": ["file_path"]
        },
    },
    }
