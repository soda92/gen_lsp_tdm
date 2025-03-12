import os
from pathlib import Path
import shutil

CURRENT = Path(__file__).resolve().parent


def tdm_cmake_init():
    cwd = os.getcwd()
    for i in os.listdir(CURRENT.joinpath("data")):
        proj_file = Path(cwd).joinpath(i)
        orig_file = CURRENT.joinpath("data").joinpath(i)
        if not proj_file.exists():
            shutil.copy(orig_file, proj_file)
