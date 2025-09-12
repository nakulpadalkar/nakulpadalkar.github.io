import pkg_resources
import subprocess
import sys

# Get all installed packages except pip
packages = [p.project_name for p in pkg_resources.working_set if p.project_name.lower() != "pip"]

for package in packages:
    print(f"Upgrading {package}...")
    subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package])
