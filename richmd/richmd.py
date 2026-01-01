"""
Markdown viewer using rich library.
Displays Markdown files with beautiful formatting in the console.
"""
import sys
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown


def main():
    if len(sys.argv) < 2:
        print("Usage: richmd.py <markdown_file>", file=sys.stderr)
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File '{file_path}' not found", file=sys.stderr)
        sys.exit(1)

    try:
        markdown_content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading file: {e}", file=sys.stderr)
        sys.exit(1)

    console = Console()
    md = Markdown(markdown_content)
    console.print(md)


if __name__ == "__main__":
    main()
