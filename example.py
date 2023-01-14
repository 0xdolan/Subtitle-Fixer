# -*- coding: utf-8 -*-

# import essential modules
import io
import sys
from pathlib import Path

# solve encoding problems
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")

# import subtitle_fixer module
from subtitle_fixer import Subtitle_Fixer

# get current directory
current_directory = Path(__file__).parent

# get all files in current directory
srt_files = current_directory.iterdir()

# make an instance of Subtitle_Fixer class
subt = Subtitle_Fixer()

# find subtitles based on their extensions
# and fix encoding of all subtitle files
fix = [
    subt.fix_encoding(s)
    for s in srt_files
    if str(s.name).split(".")[-1] in subt.subtitle_extensions
]
