import argparse
import sys
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from . import __version__


def main():
    parser = argparse.ArgumentParser(description="Markdown viewer using rich library.")
    parser.add_argument("file", nargs="?", help="Markdown file to display (default: stdin)")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = parser.parse_args()

    if args.file is None:
        try:
            markdown_content = sys.stdin.read()
        except Exception as e:
            parser.error(f"Error reading stdin: {e}")
    else:
        file_path = Path(args.file)

        if not file_path.exists():
            parser.error(f"File '{file_path}' not found")

        try:
            markdown_content = file_path.read_text(encoding='utf-8')
        except Exception as e:
            parser.error(f"Error reading file: {e}")

    console = Console()
    console.print(Markdown(markdown_content))


if __name__ == "__main__":
    main()
