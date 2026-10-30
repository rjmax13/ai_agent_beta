import os

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Write content to a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Relative path to the file"
                },
                "content": {
                    "type": "string",
                    "description": "Content to write to the file"
                }
            },
            "required": ["file_path", "content"]
        }
    }
}

def write_file(working_directory, file_path, content):

    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
        
        if not os.path.commonpath([abs_working_dir, target_dir]) == abs_working_dir:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        target_dirname = os.path.dirname(target_dir)
        if os.path.isdir(target_dir):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        
        os.makedirs(target_dirname, exist_ok=True)

        with open(target_dir, 'w') as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: Failed to write file: {e}'