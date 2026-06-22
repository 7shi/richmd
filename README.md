# richmd

Markdown viewer using rich library. Displays Markdown files with beautiful formatting in the console.

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

Show version:

```bash
richmd --version
```
