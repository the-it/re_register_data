#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

root_path = Path(__file__).parent
venv_path = root_path.joinpath("venv")
repo_path = root_path.joinpath("WS_THEbotIT")
requirements_file = repo_path.joinpath("requirements-dev.txt")

if os.name == "nt":
    global_binary = "python"
    local_binary = ".\\python"
    local_binary_path = venv_path.joinpath("Scripts")
else:
    global_binary = "python3"
    local_binary = "./python3"
    local_binary_path = venv_path.joinpath("bin")

subprocess.run([global_binary, "-m", "pip", "install", "virtualenv"])
subprocess.run([global_binary, "-m", "venv", str(venv_path)])
if not os.path.exists(repo_path):
    subprocess.run(["git", "clone", "git@github.com:the-it/WS_THEbotIT.git"], cwd=root_path)
else:
    subprocess.run(["git", "pull"], cwd=repo_path)
subprocess.run([local_binary, "-m", "pip", "install", "-r", requirements_file],
               cwd=local_binary_path)
