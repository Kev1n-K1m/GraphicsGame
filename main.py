import sys
import os

current_dir = os.getcwd()

src_dir = os.path.join(current_dir, 'src')

sys.path.append(src_dir)
from src import main
from . import ImportObject

main.main_again()