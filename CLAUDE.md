# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal learning journey repository documenting programming fundamentals week by week. Content is organized into `week1/`, `week2/`, `week3/` directories.

## Running Code

All scripts are plain Python with no external dependencies — run them directly:

```bash
python3 week1/hello.py
python3 week1/functions.py
python3 week1/loop.py
python3 week1/generate_recap.py   # generates week1/recap_day1.html
```

## Architecture

- Each week's exercises live in their own directory (`week1/`, `week2/`, etc.)
- `generate_recap.py` follows a pattern: define data structures → build HTML string → write to a `.html` file. Future recap generators should follow this same pattern.
- No build system, package manager, or test framework — this is a pure learning/scripting project.
