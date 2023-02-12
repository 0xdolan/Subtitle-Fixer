# -*- coding: utf-8 -*-

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8")


class Subtitle_Fixer:
    """Subtitle Fixer class"""

    subtitle_extensions = [
        "srt",
        "sub",
        "ssa",
        "smi",
        "vtt",
        "scc",
        "mcc",
        "ttml",
        "xml",
        "dfxp",
        "cap",
        "stl",
        "txt",
    ]

    def __init__(self):
        """Initialize the class"""

    def convert_arabic_to_persian(self, text: str) -> str:
        """convert arabic numbers to persian numbers

        :param text: text to convert
        :type text: str
        :return: converted text
        :rtype: str
        """

        arabic_chars = ["ك", "ي"]
        persian_chars = ["ک", "ی"]
        persian_numbers = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"]
        arabic_numbers = ["٠", "١", "٢", "٣", "٤", "٥", "٦", "٧", "٨", "٩"]
        mapping = dict(
            zip(arabic_numbers + arabic_chars, persian_numbers + persian_chars)
        )
        for key, value in mapping.items():
            text = text.replace(key, value)

        return text

    def fix_encoding(
        self, file_path: Path, src_encoding="windows-1256", targrt_encoding="utf-8"
    ) -> str:
        """Fix encoding of the subtitle file"""
        file_path = Path(file_path)
        file_name, file_ext = file_path.name.replace(" ", "_").rsplit(".", 1)
        fixd_name = f"{file_name.replace('.', '_')}_fixed.{file_ext}"
        if file_path.exists() and file_ext in self.subtitle_extensions:
            with open(str(file_path), "r", encoding=src_encoding) as rf:
                data = rf.read()
                data = self.convert_arabic_to_persian(data)
                # try:
                #     data = data.encode("cp1252").decode("cp1256")
                # except (UnicodeDecodeError, UnicodeEncodeError):
                #     data = data

            with open(fixd_name, "w", encoding=targrt_encoding) as wf:
                wf.write(data)

            return f"fixed file saved as {file_name}_fixed.{file_ext}"
        else:
            raise FileNotFoundError("No such file found!")
