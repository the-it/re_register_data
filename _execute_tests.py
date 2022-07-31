#!/usr/bin/env python3

import subprocess
from pathlib import Path

root_path = Path(__file__).parent
venv_path = root_path.joinpath("venv")
subprocess.run(["python3", "-m" ,"venv", str(venv_path)])
# subprocess.run(["git", "clone" ,"git@github.com:the-it/WS_THEbotIT.git"], cwd=root_path)
subprocess.run(["pwd"], cwd=root_path)
subprocess.run(["venv/bin/pip3 install -r WS_THEbotIT/requirements.txt"], cwd=root_path)
