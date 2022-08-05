import sys
import os

# Fix for relative paths
sys.path.insert(0, os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '../app')))
