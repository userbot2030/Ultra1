import os

import autopep8
import git
from pylint import epylint as lint

# Clone repository
repo_url = "https://github.com/XtomiX/Pyro-Ubott.git"
repo_dir = "https://github.com/XtomiX/Pyro-Ubott"
git.Repo.clone_from(repo_url, repo_dir)

# Go into cloned repository directory
os.chdir(repo_dir)

# Run pylint on Python files in the repository
pylint_options = ["--output-format", "json"]
pylint_stdout, pylint_stderr = lint.py_run(
    "*.py", return_std=True, arguments=pylint_options
)

# Iterate through pylint output and automatically fix issues with autopep8
for line in pylint_stdout.getvalue().split("\n"):
    if "path" in line:
        file_path = line.split(":")[0]
        with open(file_path, "r") as file:
            original_code = file.read()
        fixed_code = autopep8.fix_code(original_code)
        with open(file_path, "w") as file:
            file.write(fixed_code)

# Commit changes to the repository and push to remote
repo = git.Repo(".")
repo.git.add(".")
repo.git.commit("-m", "Automatic code formatting")
origin = repo.remote(name="origin")
origin.push()
