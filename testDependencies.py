import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEPENDENCY_DIR = os.path.join(BASE_DIR, "dependencies")
sys.path.insert(0,DEPENDENCY_DIR)
