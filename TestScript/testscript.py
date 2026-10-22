#!/usr/bin/env python3

from pathlib import Path

Path("words.txt").write_text("Linux Bash Scripting\n")
Path("numbers.txt").write_text("101 202 303\n")
print("Files created!")
variablePy = "Now I remember!"

print("\n--------------------")
for file in sorted(Path(".").glob("*.txt")):
    if file.is_file():
        text = file.read_text()
        if "Bash" in text:
            print(f"Word found in {file}")
            print(text, end="")
        else:
            print(f"Word NOT found in {file}")
        print("--------------------")
print("\nScript executed!\n")
