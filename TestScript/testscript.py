import argparse
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find a word")
    parser.add_argument("word", nargs="?", default="Bash")
    args = parser.parse_args()

    Path("words.txt").write_text("Linux Bash Scripting\n")
    Path("numbers.txt").write_text("101 202 303\n")
    print("Files created!")
    variablePy = "Now I remember!"

    print("--------------------")
    for file in sorted(Path(".").glob("*.txt")):
        if file.is_file():
            text = file.read_text()
            if args.word in text:
                print(f"Word {args.word} found in {file}")
                print(text, end="")
            else:
                print(f"Word {args.word} NOT found in {file}")
        print("--------------------")
    print("Script executed!")
