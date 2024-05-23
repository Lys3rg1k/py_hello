'''Take two parameters from the CLI. First parameter will represent a filename. 
Create a pathlib.Path object for the file, then Path.write_text the second parameter into that file.'''

import sys
from pathlib import Path

target_file = Path.cwd() / f"{sys.argv[1]}"
print(f"Name of file to write = {target_file}")
print(f"Text to write = {sys.argv[2]}")
Path(target_file).write_text(sys.argv[2])
