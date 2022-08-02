#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

root_path = Path(__file__).parent
venv_path = root_path.joinpath("venv")

if os.name == "nt":
    local_binary_path = venv_path.joinpath("Scripts")
else:
    local_binary_path = venv_path.joinpath("bin")

my_env = os.environ.copy()
my_env["WS_REAL_DATA"] = "1"
my_env["REGISTER_DATA_PATH"] = str(root_path)
subprocess.run([local_binary_path.joinpath("nose2"), "--verbosity", "0"],
               cwd=root_path,
               env=my_env)
