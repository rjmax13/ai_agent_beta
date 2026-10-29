import os
import config

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Get the content of a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Relative path to the file"
                }
            },
            "required": ["file_path"]
        }
    }
    
}

def get_file_content(working_directory: str, file_path: str) -> str:
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
    
    try:   
        if not os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        with open(target_dir, 'r') as f:
            file_content_string = f.read(config.MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
        return file_content_string

    except Exception as e:
        return f'Error: Failed to resolve target file: {e}'
    
