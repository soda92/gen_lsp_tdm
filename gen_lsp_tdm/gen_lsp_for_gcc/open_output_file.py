import subprocess
from pathlib import Path

code_cmd = r"scoop\apps\vscode\current\bin\code.cmd"
code_cmd = Path.home().joinpath(code_cmd)

file = r"C:\TDM-GCC-64\compile_commands.json"

subprocess.run(
    f"{code_cmd} {file}", shell=True, check=True
)