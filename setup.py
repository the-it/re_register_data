#!/usr/bin/env python3
import os
import subprocess  # nosec
from pathlib import Path

root_path = Path(__file__).parent
venv_path = root_path.joinpath("venv")
repo_path = root_path.joinpath("WS_THEbotIT")
requirements_file = repo_path.joinpath("requirements.txt")
requirements_dev_file = repo_path.joinpath("requirements-dev.txt")

if os.name == "nt":
    global_binary = "python"
    local_binary_path = venv_path.joinpath("Scripts")
    local_binary = local_binary_path.joinpath("python")
else:
    global_binary = "python3"
    local_binary_path = venv_path.joinpath("bin")
    local_binary = local_binary_path.joinpath("python3")

subprocess.run([global_binary, "-m", "pip", "install", "virtualenv"])  # nosec
subprocess.run([global_binary, "-m", "venv", str(venv_path)])  # nosec
if not os.path.exists(repo_path):
    subprocess.run(["git", "clone", "https://github.com/the-it/WS_THEbotIT.git"], cwd=root_path)  # nosec
else:
    subprocess.run(["git", "pull"], cwd=repo_path)  # nosec
subprocess.run([local_binary, "-m", "pip", "install",
                "-r", requirements_file,
                "-r", requirements_dev_file],  # nosec
               cwd=local_binary_path)
