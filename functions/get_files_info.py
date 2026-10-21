import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))

    try:   
        if not os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{target_dir}" is not a directory'
        return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f'Error: Failed to resolve target directory: {e}'
    
