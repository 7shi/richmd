# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Pipe the output through a pager (`$PAGER`, default `less` with `LESS=FRX`) when stdout is a terminal, like `git`, with colors always emitted. Use `--no-pager` (implied when stdout is piped or redirected) to print directly

## [0.2.0] - 2026-06-23

### Changed
- Added `--version` option to display the package version
- Support reading from stdin when no file is specified

## [0.1.0] - 2026-01-01

### Added
- Initial release
