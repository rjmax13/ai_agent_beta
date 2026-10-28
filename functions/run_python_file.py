import os
import subprocess

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    timeout = 30
    if args is None:
        args = []
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))

        if not os.path.commonpath([abs_working_dir, target_file]) == abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'


        result = subprocess.run(
            ["python", target_file, *args],
            cwd=abs_working_dir,
            capture_output=True,
            text=True,
            timeout=timeout
        )

        if result.stdout == "" and result.stderr == "":
            return "No output produced"
        if result.returncode != 0:
            return f'Process exited with code {result.returncode}\nSTDOUT: {result.stdout}\nSTDERR: {result.stderr}'
            
        return f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"

    except Exception as e:
        return f'Error: executing Python file: {e}'
