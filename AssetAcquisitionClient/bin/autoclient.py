"--wallace--"
import os
import sys

from src.scripts import client

BASE_DIR = os.path.dirname(os.path.dirname(os.path.basename(__file__)))
sys.path.append(BASE_DIR)


if __name__ == '__main__':
    client()