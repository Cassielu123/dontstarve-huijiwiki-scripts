import sys
import os
import importlib

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT)
DST_ROOT = importlib.import_module("main").dst_path


SCRIPTS_PATH = DST_ROOT / "data" / "databundles" / "scripts.zip"
VERSION_PATH = DST_ROOT / "version.txt"

if not VERSION_PATH.exists():
    DST_VERSION = None
else:
    with open(VERSION_PATH, "r") as f:
        DST_VERSION = f.read().strip()

CURRENT_DIR = os.path.dirname(__file__)
SKILLTREE_OUTPUT_DIR = os.path.join(CURRENT_DIR, "skilltrees")
