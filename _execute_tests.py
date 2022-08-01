#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

root_path = Path(__file__).parent
venv_path = root_path.joinpath("venv")
repo_path = root_path.joinpath("WS_THEbotIT")
subprocess.run(["python3", "-m" ,"venv", str(venv_path)])
if not os.path.exists(repo_path):
    subprocess.run(["git", "clone", "git@github.com:the-it/WS_THEbotIT.git"], cwd=root_path)
else:
    subprocess.run(["git", "pull"], cwd=repo_path)
subprocess.run(["./python3", "-m", "pip", "install", "-r", repo_path.joinpath("requirements-dev.txt")], cwd=venv_path.joinpath("bin"))

my_env = os.environ.copy()
my_env["WS_REAL_DATA"] = "1"
subprocess.run(["venv/bin/nose2", "--verbosity", "0"], cwd=root_path, env=my_env)
