# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

Personal LeetCode practice repo working through the [Neetcode 150](https://neetcode.io/practice) checklist. Progress is tracked in `README.md`.

## Running Solutions

**Python:**
```bash
python3 Problem-<N>/<file>.py
```

**C++ (compile then run):**
```bash
clang -fcolor-diagnostics -fansi-escape-codes -g Problem-<N>/<file>.cpp -o Problem-<N>/<binary>
./Problem-<N>/<binary>
```

The Python venv at `leetcode/` is Python 3.14 — activate with `source leetcode/bin/activate` if needed.

## File Conventions

Each solution file follows this header pattern:
```python
# https://leetcode.com/problems/<slug>/
# SOLVED
# Time Complexity - O(...)
# Space Complexity - O(...)
```

Solutions embed their own test cases in a `main()` block (Python) or `main()` function (C++), printing expected vs. actual output. No external test framework is used.

## Directory Structure

Each problem lives in `Problem-<number>/` with one or more solution files. Some directories contain compiled binaries (`a.out`, `<name>`) and `tempCodeRunnerFile.cpp` artifacts — these are gitignored-by-convention but may appear locally.

## Commit Style

Commits follow: `Problem <N> Complete -- Time Comp: O(...) -- Space Comp: O(...)`
