import subprocess
from pathlib import Path

code_cmd = r"scoop\apps\vscode\current\bin\code.cmd"
code_cmd = Path.home().joinpath(code_cmd)

file = r"C:\TDM-GCC-64\virtual\lib\gcc\x86_64-w64-mingw32\10.3.0\include\c++\iostream"

subprocess.run(
    f"{code_cmd} {file}", shell=True, check=True
)