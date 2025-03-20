import json
import glob

from pathlib import Path
from sodatools import write_path, str_path, read_path


def get_file_list(i: str):
    lis = list(glob.glob("**/*", recursive=True, root_dir=i))
    ret = []
    for p in lis:
        ret.append(Path(i).joinpath(p))
    # print(i)
    return ret


def fix_content(c):
    c = c.replace("__MINGW_ATTRIB_NORETURN", "")
    c = c.replace("__MINGW_NOTHROW", "")
    return c


def write_virtual(f):
    if f.is_dir():
        return
    global cnt
    base = Path(r"c:\TDM-GCC-64")
    virtual = Path(r"c:\TDM-GCC-64\virtual")
    rel = Path(f).relative_to(base)
    vfile = virtual.joinpath(rel)

    vfile.parent.mkdir(parents=True, exist_ok=True)

    try:
        c = fix_content(read_path(f))
        write_path(vfile, c)
    except UnicodeDecodeError:
        return

    if vfile == Path(r"C:\TDM-GCC-64\virtual\x86_64-w64-mingw32\include\_mingw.h"):
        write_path(vfile, read_path(vfile).replace("#define \n", ""))


def lsp_init():
    tdm_dir = r"c:/TDM-GCC-64"
    tdm_dir_v = r"c:/TDM-GCC-64/virtual"
    Path(tdm_dir_v).mkdir()
    db = Path(tdm_dir_v).joinpath("compile_commands.json")

    dirs = [
        r"{gcc}lib/gcc/x86_64-w64-mingw32/10.3.0/include/c++",
        r"{gcc}x86_64-w64-mingw32/include",
        r"{gcc}lib/gcc/x86_64-w64-mingw32/10.3.0/include/c++/x86_64-w64-mingw32",
    ]

    includes_list = []

    for i in dirs:
        i = i.replace("\\", "/")
        _source = i.replace("{gcc}", tdm_dir + "/")
        virtual = i.replace("{gcc}", tdm_dir_v + "/")
        includes_list.append("-isystem " + virtual)
    includes = " ".join(includes_list)

    objs = []

    dummy_cc = str_path(Path(tdm_dir_v).joinpath("demo.cc"))
    write_path(Path(dummy_cc), "")

    for i in dirs:
        i = i.replace("\\", "/")
        i = i.replace("{gcc}", tdm_dir + "/")
        files = get_file_list(i)

        for f in files:
            write_virtual(f)

        obj = {
            "directory": tdm_dir_v,
            "command": f"C:/TDM-GCC-64/bin/g++.exe {includes} {dummy_cc}",
            "file": dummy_cc,
            "output": str_path(Path(tdm_dir_v).joinpath("a.obj")),
        }
        objs.append(obj)

    s = json.dumps(objs, indent=2)
    write_path(db, s)
