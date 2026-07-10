#!/usr/bin/env python3
import os
import subprocess  # nosec
from pathlib import Path

root_path = Path(__file__).resolve().parent
venv_path = root_path.joinpath("venv")
repo_path = root_path.joinpath("WS_THEbotIT")

# download or update the bot repository with the test code
if not os.path.exists(repo_path):
    subprocess.run(["git", "clone", "https://github.com/the-it/WS_THEbotIT.git"], cwd=root_path)  # nosec
else:
    subprocess.run(["git", "pull"], cwd=repo_path)  # nosec

# let uv create the virtual environment and install the project incl. dev dependencies.
# UV_PROJECT_ENVIRONMENT points uv to the local "venv" directory so that test.py keeps working.
sync_env = os.environ.copy()
sync_env["UV_PROJECT_ENVIRONMENT"] = str(venv_path)
subprocess.run(["uv", "sync", "--all-extras"],  # nosec
               cwd=repo_path,
               env=sync_env)