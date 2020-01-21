import subprocess
import sys

def install(package):
    """Installs a python package"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
    
