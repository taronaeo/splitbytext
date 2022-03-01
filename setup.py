from cx_Freeze import setup, Executable

base = None
executables = [Executable("main.py", target_name='splitbytext.exe', base=base)]

packages = [
  "os",
  "time",
  "colorama",
  "InquirerPy",
  "PyPDF2"
]

options = {
  "build_exe": {
    "packages": packages
  }
}

setup(
  name = "splitbytext",
  options = options,
  version = "1.0",
  description = "",
  executables = executables,
)