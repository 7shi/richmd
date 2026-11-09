# richmd

Markdown viewer using rich library. Displays Markdown files with beautiful formatting in the console.

> [!NOTE]
> This project is no longer under development. For viewing Markdown in the terminal, [leaf](https://github.com/rivolink/leaf) is recommended instead.

## Requirements

- Python >= 3.10

## Installation

### As a tool (recommended)

```bash
# Install as a tool
uv tool install https://github.com/7shi/richmd.git

# Add ~/.local/bin to PATH if not already added
export PATH="$HOME/.local/bin:$PATH"
```

### From source

```bash
# Source installation with uv
git clone https://github.com/7shi/richmd.git
cd richmd
uv sync
```

**Note**: When using source installation, prefix all commands with `uv run` (e.g., `uv run richmd`).

## Usage

```bash
richmd <markdown_file>
```

Read from stdin:

```bash
cat <markdown_file> | richmd
```

Like `git`, the output is piped through a pager when stdout is a terminal, with colors always emitted. The pager is taken from `$PAGER` (default `less`); if `LESS` is unset, it is set to `FRX` so short output is printed without entering the pager and colors are shown. Set `PAGER=cat` to disable the pager (colors are still emitted). Pass `--no-pager` to print directly without the pager; rich then decides whether to use colors. This is implied when stdout is piped or redirected.

```bash
richmd --no-pager <markdown_file>
```

Show version:

```bash
richmd --version
```
