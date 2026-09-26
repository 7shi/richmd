import argparse
import os
import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from . import __version__


def page(text: str) -> None:
    # Mimic git: let an empty PAGER or "cat" mean "no pager". LESS=FRX makes
    # less exit immediately if the text fits on one screen (F), keep ANSI
    # colors raw (R), and not clear the screen on exit (X). Respect a
    # user-set LESS as git does
    pager = os.environ.get("PAGER", "less")
    if pager.strip() in ("", "cat"):
        sys.stdout.write(text)
        return
    env = dict(os.environ)
    env.setdefault("LESS", "FRX")
    try:
        # shell=True so PAGER may carry arguments (e.g. "less -S")
        proc = subprocess.Popen(pager, shell=True, stdin=subprocess.PIPE, env=env)
    except OSError:
        sys.stdout.write(text)
        return
    try:
        proc.stdin.write(text.encode(sys.stdout.encoding or "utf-8", errors="replace"))
        proc.stdin.close()
    except BrokenPipeError:
        # The user quit the pager before reading everything
        pass
    # Ctrl-C belongs to the pager while it runs; keep waiting for it to exit
    while True:
        try:
            proc.wait()
            break
        except KeyboardInterrupt:
            pass


def main():
    parser = argparse.ArgumentParser(description="Markdown viewer using rich library.")
    parser.add_argument("file", nargs="?", help="Markdown file to display (default: stdin)")
    parser.add_argument("--no-pager", action="store_true", help="do not pipe output into a pager")
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

    markdown = Markdown(markdown_content)
    try:
        if not args.no_pager and sys.stdout.isatty():
            # Like git, page only when stdout is a terminal. Render into a
            # string with colors forced on and hand it to the pager (less -R
            # shows them)
            console = Console(force_terminal=True)
            with console.capture() as capture:
                console.print(markdown)
            page(capture.get())
        else:
            # --no-pager, or piped or redirected: print directly, letting
            # rich decide whether to use colors
            Console().print(markdown)
    except BrokenPipeError:
        os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())


if __name__ == "__main__":
    main()
